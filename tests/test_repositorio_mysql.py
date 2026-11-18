"""Testes de integração do repositório MySQL (src/repositorios/repositorio_pessoas_mysql.py).

Usam o servidor configurado pelas variáveis MYSQL_* e o banco cadastro_pessoas_teste.
São ignorados quando o PyMySQL não está instalado ou o servidor não está acessível.
"""

import pytest

pymysql = pytest.importorskip("pymysql")

# pylint: disable=wrong-import-position
from cadastro import CadastroPessoa
from pessoa import Pessoa
from repositorios.repositorio_pessoas_mysql import ConfiguracaoMysql, RepositorioPessoasMysql

BANCO_TESTE = "cadastro_pessoas_teste"


@pytest.fixture(name="repositorio")
def FixtureRepositorio():
    """Retorna um repositório MySQL com a tabela de pessoas vazia."""
    configuracao = ConfiguracaoMysql()
    configuracao.banco = BANCO_TESTE
    try:
        repositorio = RepositorioPessoasMysql(configuracao)
    except pymysql.err.OperationalError as erro:
        pytest.skip(f"MySQL indisponível: {erro}")

    conexao = pymysql.connect(
        host=configuracao.host,
        port=configuracao.porta,
        user=configuracao.usuario,
        password=configuracao.senha,
        database=configuracao.banco,
        autocommit=True,
    )
    with conexao.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE pessoas")
    conexao.close()
    return repositorio


class TestRepositorioPessoasMysql:
    """Testes das operações do repositório MySQL."""

    def testListarRepositorioVazio(self, repositorio):
        """Um repositório sem cadastros deve retornar uma lista vazia."""
        assert not repositorio.listar()

    def testCadastrarEListarMantemOrdem(self, repositorio):
        """As pessoas devem ser listadas na ordem em que foram cadastradas."""
        repositorio.cadastrar(Pessoa("Ana", 25, "ana@gmail.com"))
        repositorio.cadastrar(Pessoa("Bruno", 16, "bruno@outlook.com"))

        pessoas = repositorio.listar()

        assert [pessoa.getNome() for pessoa in pessoas] == ["Ana", "Bruno"]
        assert pessoas[1].getIdade() == 16
        assert pessoas[1].getEmail() == "bruno@outlook.com"

    def testBuscarPorNomeExistente(self, repositorio):
        """Buscar um nome cadastrado deve retornar os dados da pessoa."""
        repositorio.cadastrar(Pessoa("Ana", 25, "ana@gmail.com"))

        pessoa = repositorio.buscar("Ana")

        assert pessoa is not None
        assert pessoa.getIdade() == 25
        assert pessoa.getEmail() == "ana@gmail.com"

    def testBuscarPorNomeInexistente(self, repositorio):
        """Buscar um nome não cadastrado deve retornar None."""
        assert repositorio.buscar("Zeca") is None

    def testAlterarPessoaExistente(self, repositorio):
        """Alterar deve substituir os dados gravados no banco."""
        repositorio.cadastrar(Pessoa("Ana", 25, "ana@gmail.com"))
        repositorio.cadastrar(Pessoa("Bruno", 16, "bruno@outlook.com"))

        alterou = repositorio.alterar("Bruno", Pessoa("Bruno Lima", 17, "bruno@gmail.com"))

        assert alterou
        assert repositorio.buscar("Bruno") is None
        assert repositorio.buscar("Bruno Lima").getIdade() == 17
        assert repositorio.buscar("Ana").getIdade() == 25

    def testAlterarSemMudarOsDados(self, repositorio):
        """Alterar com os mesmos dados deve indicar que a pessoa foi encontrada."""
        repositorio.cadastrar(Pessoa("Ana", 25, "ana@gmail.com"))

        assert repositorio.alterar("Ana", Pessoa("Ana", 25, "ana@gmail.com"))

    def testAlterarPessoaInexistente(self, repositorio):
        """Alterar uma pessoa não cadastrada deve retornar False."""
        assert not repositorio.alterar("Zeca", Pessoa("Zeca", 40, "zeca@gmail.com"))

    def testCadastroPersisteAlteracaoNoBanco(self, repositorio):
        """O CadastroPessoa deve gravar no banco as alterações feitas na pessoa."""
        cadastro = CadastroPessoa(repositorio)
        cadastro.cadastrar("Ana", 25, "ana@gmail.com")

        cadastro.alterar("Ana", "Ana Maria", 26, "anamaria@outlook.com")

        pessoa = repositorio.buscar("Ana Maria")
        assert pessoa is not None
        assert pessoa.getEmail() == "anamaria@outlook.com"
