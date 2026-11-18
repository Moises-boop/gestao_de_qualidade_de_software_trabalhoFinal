"""Repositório de pessoas armazenadas em um banco de dados MySQL."""

import os
from contextlib import contextmanager
from typing import Iterator, List, Optional

import pymysql
from pymysql.constants import CLIENT

from pessoa import Pessoa
from repositorios.repositorio_pessoas import RepositorioPessoas

HOST_PADRAO = "127.0.0.1"
PORTA_PADRAO = 3307
USUARIO_PADRAO = "root"
BANCO_PADRAO = "cadastro_pessoas"

SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS pessoas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL,
        email VARCHAR(255) NOT NULL,
        INDEX idx_pessoas_nome (nome)
    )
"""
SQL_INSERIR = "INSERT INTO pessoas (nome, idade, email) VALUES (%s, %s, %s)"
SQL_BUSCAR = "SELECT nome, idade, email FROM pessoas WHERE nome = %s ORDER BY id LIMIT 1"
SQL_LISTAR = "SELECT nome, idade, email FROM pessoas ORDER BY id"
SQL_ALTERAR = (
    "UPDATE pessoas SET nome = %s, idade = %s, email = %s "
    "WHERE nome = %s ORDER BY id LIMIT 1"
)


class ConfiguracaoMysql:  # pylint: disable=too-few-public-methods
    """Dados de conexão com o MySQL, lidos das variáveis de ambiente.

    Variáveis: MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD e MYSQL_DATABASE.
    Os valores padrão apontam para o servidor principal do infra/compose.yaml.
    """

    def __init__(self) -> None:
        self.host = os.environ.get("MYSQL_HOST", HOST_PADRAO)
        self.porta = int(os.environ.get("MYSQL_PORT", str(PORTA_PADRAO)))
        self.usuario = os.environ.get("MYSQL_USER", USUARIO_PADRAO)
        self.senha = os.environ.get("MYSQL_PASSWORD", "")
        self.banco = os.environ.get("MYSQL_DATABASE", BANCO_PADRAO)


class RepositorioPessoasMysql(RepositorioPessoas):
    """Guarda as pessoas na tabela `pessoas` de um banco MySQL.

    O banco e a tabela são criados, caso não existam, ao instanciar o repositório.
    """

    def __init__(self, configuracao: Optional[ConfiguracaoMysql] = None) -> None:
        self.__configuracao = configuracao or ConfiguracaoMysql()
        self.__criarEstrutura()

    def __conectar(self, com_banco: bool = True) -> pymysql.connections.Connection:
        """Abre uma nova conexão com o servidor, com ou sem o banco selecionado."""
        configuracao = self.__configuracao
        return pymysql.connect(
            host=configuracao.host,
            port=configuracao.porta,
            user=configuracao.usuario,
            password=configuracao.senha,
            database=configuracao.banco if com_banco else None,
            charset="utf8mb4",
            autocommit=True,
            # Faz o UPDATE informar as linhas encontradas, mesmo sem mudança nos valores
            client_flag=CLIENT.FOUND_ROWS,
        )

    @contextmanager
    def __cursor(self, com_banco: bool = True) -> Iterator[pymysql.cursors.Cursor]:
        """Fornece um cursor e fecha a conexão ao final do bloco."""
        conexao = self.__conectar(com_banco)
        try:
            with conexao.cursor() as cursor:
                yield cursor
        finally:
            conexao.close()

    def __criarEstrutura(self) -> None:
        """Cria o banco e a tabela de pessoas, caso ainda não existam."""
        with self.__cursor(com_banco=False) as cursor:
            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS `{self.__configuracao.banco}` "
                "CHARACTER SET utf8mb4"
            )
        with self.__cursor() as cursor:
            cursor.execute(SQL_CRIAR_TABELA)

    def cadastrar(self, pessoa: Pessoa) -> None:
        with self.__cursor() as cursor:
            cursor.execute(SQL_INSERIR, (pessoa.getNome(), pessoa.getIdade(), pessoa.getEmail()))

    def buscar(self, nome: str) -> Optional[Pessoa]:
        with self.__cursor() as cursor:
            cursor.execute(SQL_BUSCAR, (nome,))
            linha = cursor.fetchone()
        if linha is None:
            return None
        return Pessoa(*linha)

    def listar(self) -> List[Pessoa]:
        with self.__cursor() as cursor:
            cursor.execute(SQL_LISTAR)
            linhas = cursor.fetchall()
        return [Pessoa(*linha) for linha in linhas]

    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        with self.__cursor() as cursor:
            linhas_alteradas = cursor.execute(SQL_ALTERAR, (
                nova_pessoa.getNome(), nova_pessoa.getIdade(), nova_pessoa.getEmail(), nome,
            ))
        return linhas_alteradas > 0
