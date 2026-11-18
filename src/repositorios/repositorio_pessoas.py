"""Contrato dos repositórios de pessoas."""

from abc import ABC, abstractmethod
from typing import List, Optional

from pessoa import Pessoa


class RepositorioPessoas(ABC):
    """Define as operações de armazenamento de pessoas."""

    @abstractmethod
    def cadastrar(self, pessoa: Pessoa) -> None:
        """Armazena uma nova pessoa."""

    @abstractmethod
    def buscar(self, nome: str) -> Optional[Pessoa]:
        """Retorna a primeira pessoa com o nome informado, ou None se não houver."""

    @abstractmethod
    def listar(self) -> List[Pessoa]:
        """Retorna todas as pessoas, na ordem em que foram cadastradas."""

    @abstractmethod
    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        """Substitui os dados da pessoa com o nome informado.

        Retorna True se a pessoa foi encontrada e alterada, e False caso contrário.
        """
