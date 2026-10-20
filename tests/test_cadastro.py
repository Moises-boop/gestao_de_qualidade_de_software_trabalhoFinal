"""Testes automatizados dos serviços do cadastro de pessoas (src/cadastro.py)."""

import pytest

from cadastro import CadastroPessoa


@pytest.fixture(name="cadastro")
def FixtureCadastro():
    """Retorna um cadastro vazio, novo a cada teste."""
    return CadastroPessoa()


@pytest.fixture(name="cadastro_preenchido")
def FixtureCadastroPreenchido(cadastro):
    """Retorna um cadastro com duas pessoas já cadastradas."""
    cadastro.cadastrar("Ana", 25, "ana@gmail.com")
    cadastro.cadastrar("Bruno", 16, "bruno@outlook.com")
    return cadastro


class TestOperacoesCadastro:
    """Testes das operações de cadastrar, buscar, listar e alterar."""

    def testCadastrarRetornaPessoaComOsDadosInformados(self, cadastro):
        """Cadastrar deve criar a pessoa com nome, idade e e-mail informados."""
        pessoa = cadastro.cadastrar("Carlos", 30, "carlos@gmail.com")

        assert pessoa.getNome() == "Carlos"
        assert pessoa.getIdade() == 30
        assert pessoa.getEmail() == "carlos@gmail.com"

    def testCadastrarAdicionaPessoaNaLista(self, cadastro):
        """A pessoa cadastrada deve aparecer na listagem."""
        pessoa = cadastro.cadastrar("Carlos", 30, "carlos@gmail.com")

        assert cadastro.listar() == [pessoa]

    def testListarCadastroVazio(self, cadastro):
        """Um cadastro novo não deve ter pessoas."""
        assert not cadastro.listar()

    def testListarMantemOrdemDeCadastro(self, cadastro_preenchido):
        """A listagem deve retornar as pessoas na ordem em que foram cadastradas."""
        nomes = [pessoa.getNome() for pessoa in cadastro_preenchido.listar()]

        assert nomes == ["Ana", "Bruno"]

    def testBuscarPorNomeExistente(self, cadastro_preenchido):
        """Buscar um nome cadastrado deve retornar a pessoa correspondente."""
        pessoa = cadastro_preenchido.buscarPorNome("Bruno")

        assert pessoa is not None
        assert pessoa.getEmail() == "bruno@outlook.com"

    def testBuscarPorNomeInexistente(self, cadastro_preenchido):
        """Buscar um nome não cadastrado deve retornar None."""
        assert cadastro_preenchido.buscarPorNome("Zeca") is None

    def testAlterarPessoaExistente(self, cadastro_preenchido):
        """Alterar deve substituir todos os dados da pessoa."""
        pessoa = cadastro_preenchido.alterar("Ana", "Ana Maria", 26, "anamaria@outlook.com")

        assert pessoa.getNome() == "Ana Maria"
        assert pessoa.getIdade() == 26
        assert pessoa.getEmail() == "anamaria@outlook.com"
        assert cadastro_preenchido.buscarPorNome("Ana") is None
        assert cadastro_preenchido.buscarPorNome("Ana Maria") is pessoa

    def testAlterarPessoaInexistente(self, cadastro_preenchido):
        """Alterar uma pessoa não cadastrada deve retornar None e não mudar o cadastro."""
        resultado = cadastro_preenchido.alterar("Zeca", "Novo", 40, "novo@gmail.com")

        assert resultado is None
        assert len(cadastro_preenchido.listar()) == 2


class TestAnalisesCadastro:
    """Testes das regras de análise de situação, faixa etária, e-mail e contato."""

    @pytest.mark.parametrize("idade, esperado", [
        (17, "Menor de idade"),
        (18, "Maior de idade"),
        (60, "Maior de idade"),
    ])
    def testSituacao(self, cadastro, idade, esperado):
        """A maioridade começa exatamente aos 18 anos."""
        pessoa = cadastro.cadastrar("Teste", idade, "teste@gmail.com")

        assert cadastro.situacao(pessoa) == esperado

    @pytest.mark.parametrize("idade, esperado", [
        (0, "crianca"),
        (11, "crianca"),
        (12, "adolescente"),
        (17, "adolescente"),
        (18, "adulto"),
        (59, "adulto"),
        (60, "idoso"),
        (90, "idoso"),
    ])
    def testAnalisarFaixaEtaria(self, cadastro, idade, esperado):
        """Cada faixa etária deve ser respeitada nos seus limites."""
        pessoa = cadastro.cadastrar("Teste", idade, "teste@gmail.com")

        assert cadastro.analisarFaixaEtaria(pessoa) == esperado

    @pytest.mark.parametrize("email, esperado", [
        ("ana@gmail.com", "Gmail"),
        ("ana@outlook.com", "Outlook"),
        ("ana@utfpr.edu.br", "outro"),
        ("ana.gmail.com", "e-mail invalido"),
        ("", "e-mail invalido"),
    ])
    def testAnalisarEmail(self, cadastro, email, esperado):
        """O provedor deve ser identificado pelo domínio, e e-mails sem @ são inválidos."""
        pessoa = cadastro.cadastrar("Teste", 30, email)

        assert cadastro.analisarEmail(pessoa) == esperado

    @pytest.mark.parametrize("idade, email, esperado", [
        (17, "ana@gmail.com", "menor de idade"),
        (17, "ana.gmail.com", "menor de idade"),
        (18, "ana.gmail.com", "e-mail invalido"),
        (18, "ana@gmail.com", "completo"),
    ])
    def testAnalisarContato(self, cadastro, idade, email, esperado):
        """A idade é verificada antes do e-mail na análise de contato."""
        pessoa = cadastro.cadastrar("Teste", idade, email)

        assert cadastro.analisarContato(pessoa) == esperado
