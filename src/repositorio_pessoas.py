from abc import ABC, abstractmethod
from typing import List, Optional

from pessoa import Pessoa

class RepositorioPessoas(ABC):
    @abstractmethod
    def cadastrar(self, pessoa: Pessoa) -> None:
        pass

    @abstractmethod
    def buscar(self, nome: str) -> Optional[Pessoa]:
        pass

    @abstractmethod
    def listar(self) -> List[Pessoa]:
        pass

    @abstractmethod
    def alterar(self, nome: str, nova_pessoa) -> bool:
        pass