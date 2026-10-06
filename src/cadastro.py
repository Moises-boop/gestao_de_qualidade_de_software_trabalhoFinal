"""Serviços (casos de uso) do cadastro de pessoas.

Reúne as operações sobre a classe Pessoa, sem interação com o usuário.

Artefato didático que serve de suporte para a disciplina de Gestão de
Qualidade de Software, curso de Ciência da Computação - UTFPR campus Medianeira.
"""

from pessoa import Pessoa

MAIORIDADE = 18

class CadastroPessoa:
    """Gerencia o conjunto de pessoas cadastradas"""

    def __init__(self):
        self.__pessoas = []

    def cadastrar(self, nome, idade, email):
        """Cria uma pessoa com os dados informados e a adiciona ao cadastro."""
        pessoa = Pessoa(nome, idade, email)
        self.__pessoas.append(pessoa)
        return pessoa

    def buscarPorNome(self, nome):
        """Retorna a pessoa com o nome informado, ou None se não estiver cadastrada."""
        for pessoa in self.__pessoas:
            if pessoa.getNome() == nome:
                return pessoa
        return None

    def listar(self):
        """Retorna a lista de pessoas cadastradas."""
        return self.__pessoas

    def alterar(self, nome, novo_nome, nova_idade, novo_email):
        """Substitui os dados da pessoa com o nome informado.

        Retorna a pessoa alterada, ou None se não estiver cadastrada.
        """
        pessoa = self.buscarPorNome(nome)

        if pessoa is None:
            return None

        pessoa.setNome(novo_nome)
        pessoa.setIdade(nova_idade)
        pessoa.setEmail(novo_email)

        return pessoa

    def situacao(self, pessoa):
        """Retorna a situação da pessoa (maior ou menor de idade) de acordo com a idade."""
        if pessoa.getIdade() >= MAIORIDADE:
            return "Maior de idade"
        return "Menor de idade"

    def analisarFaixaEtaria(self, pessoa):
        """Retorna a faixa etária correspondente à idade da pessoa."""
        idade = pessoa.getIdade()
        if idade < 12:
            return "crianca"
        if idade < MAIORIDADE:
            return "adolescente"
        if idade < 60:
            return "adulto"
        return "idoso"

    def analisarEmail(self, pessoa):
        """Retorna o provedor do e-mail da pessoa, ou indica que o e-mail é inválido."""
        email = pessoa.getEmail()
        if "@" not in email:
            return "e-mail invalido"
        if email.endswith("@gmail.com"):
            return "Gmail"
        if email.endswith("@outlook.com"):
            return "Outlook"
        return "outro"

    def analisarContato(self, pessoa):
        """Retorna a situação do contato considerando a idade e a validade do e-mail."""
        if pessoa.getIdade() < MAIORIDADE:
            return "menor de idade"
        if "@" not in pessoa.getEmail():
            return "e-mail invalido"
        return "completo"
