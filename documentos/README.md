# gqs-cadastro-pessoas
Projeto evolutivo de cadastro de pessoas em Python, utilizado na disciplina Gestão da Qualidade de Software para práticas de modularização, qualidade de código e versionamento com Git.

Projeto desenvolvido na disciplina **Gestão da Qualidade de Software**.

O sistema implementa um cadastro simples de pessoas em Python e será utilizado como artefato de estudo e evolução ao longo da disciplina.

## Objetivo

Utilizar um mesmo projeto para aplicar, progressivamente, conceitos e práticas relacionados à qualidade de software.

## Tecnologias

- Python
- PyTest
- MySQL (PyMySQL e Docker Compose)
- Git
- GitHub

## Estrutura

- `documentos/`: README, guia de contribuição (`CONTRIBUTING.md`) e checklist de inspeção.
- `src/pessoa.py`: classe `Pessoa`, com os dados de uma pessoa.
- `src/cadastro.py`: serviços (casos de uso) do cadastro, como cadastrar, buscar, listar, alterar e analisar pessoas.
- `src/repositorios/`: armazenamento das pessoas, em memória ou em MySQL.
- `src/main.py`: interface em console com o usuário (menu, leitura e exibição dos dados).
- `infra/compose.yaml`: servidores MySQL (principal e réplica) para o Docker Compose.
- `tests/test_cadastro.py`: testes automatizados dos serviços do cadastro.
- `tests/test_repositorio_mysql.py`: testes de integração do repositório MySQL.
- `pytest.ini`: configuração do PyTest.

## Execução

Execute o programa pelo terminal, a partir da raiz do projeto:

```bash
cd src
python main.py
```

Por padrão os dados ficam em memória. Para gravá-los no MySQL, suba o banco e informe o repositório e a senha:

```bash
docker compose -f infra/compose.yaml up -d
export CADASTRO_REPOSITORIO=mysql MYSQL_PASSWORD=<senha do compose>
cd src
python main.py
```

As demais variáveis de conexão estão descritas no `CONTRIBUTING.md`.

## Testes

Com o ambiente virtual ativado, execute a partir da raiz do projeto:

```bash
pytest
```
