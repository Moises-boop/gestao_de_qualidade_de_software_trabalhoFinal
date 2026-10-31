"""Serviços (casos de uso) do cadastro de pessoas.

Reúne as operações sobre a classe Pessoa, sem interação com o usuário.

Artefato didático que serve de suporte para a disciplina de Gestão de
Qualidade de Software, curso de Ciência da Computação - UTFPR campus Medianeira.
"""

from typing import List, Optional

from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas
from repositorio_pessoas_memoria import RepositorioPessoasMemoria

IDADE_ADOLESCENTE = 12
MAIORIDADE = 18
IDADE_IDOSO = 60

class CadastroPessoa:
    """Gerencia o conjunto de pessoas cadastradas."""

    def __init__(self, repositorio: Optional[RepositorioPessoas] = None) -> None:
        if repositorio is None:
            repositorio = RepositorioPessoasMemoria()

        self.__repositorio = repositorio

    def cadastrar(self, nome, idade, email):
        pessoa = Pessoa(nome, idade, email)
        self.__repositorio.cadastrar(pessoa)
        return pessoa

    def buscarPorNome(self, nome):
        return self.__repositorio.buscar(nome)

    def listar(self) -> List[Pessoa]:
        return self.__repositorio.listar()

    def alterar(self, nome, novo_nome, nova_idade, novo_email):
        pessoa = self.buscarPorNome(nome)

        if pessoa is None:
            return None

        pessoa.setNome(novo_nome)
        pessoa.setIdade(nova_idade)
        pessoa.setEmail(novo_email)

        return pessoa

    def situacao(self, pessoa):
        """Retorna a situação da pessoa de acordo com a idade."""
        if pessoa.getIdade() >= MAIORIDADE:
            return "Maior de idade"
        return "Menor de idade"

    def analisarFaixaEtaria(self, pessoa):
        """Retorna a faixa etária correspondente à idade da pessoa."""
        idade = pessoa.getIdade()

        if idade < IDADE_ADOLESCENTE:
            return "crianca"
        if idade < MAIORIDADE:
            return "adolescente"
        if idade < IDADE_IDOSO:
            return "adulto"
        return "idoso"

    def analisarEmail(self, pessoa):
        """Retorna o provedor do e-mail ou indica se é inválido."""
        email = pessoa.getEmail()

        if "@" not in email:
            return "e-mail invalido"
        if email.endswith("@gmail.com"):
            return "Gmail"
        if email.endswith("@outlook.com"):
            return "Outlook"
        return "outro"

    def analisarContato(self, pessoa):
        """Retorna a situação do contato considerando idade e e-mail."""
        if pessoa.getIdade() < MAIORIDADE:
            return "menor de idade"
        if "@" not in pessoa.getEmail():
            return "e-mail invalido"
        return "completo"
    