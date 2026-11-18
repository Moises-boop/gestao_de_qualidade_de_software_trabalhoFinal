# Padronizações de nomenclaturas e boas práticas para a concepção deste software

## Nomenclatura e estilo

1. Nomes de variáveis e de argumentos no formato *snake_case*.
2. Nomes de funções em *PascalCase*.
3. Linhas de no máximo 100 caracteres.
4. **docstrings** devem estar presentes nos módulos, classes, funções e métodos.
5. Constantes em MAÍUSCULO.
6. Classes em *PascalCase*.
7. Métodos em *camelCase*.
8. Atributos em *snake_case*.
9. Nomes de módulos (arquivos `.py`) em *snake_case*.

## Organização do código

O código fica na pasta `src`, os testes na pasta `tests`, a documentação na pasta `documentos`, e o código é dividido em camadas:

- `pessoa.py`: classe `Pessoa`, que guarda os dados de uma pessoa (atributos privados, acessados por *getters* e *setters*).
- `cadastro.py`: classe `CadastroPessoa`, com os serviços (casos de uso) do sistema, como cadastrar, buscar, listar, alterar e analisar pessoas.
- `repositorios/`: pacote com o armazenamento das pessoas.
  - `repositorio_pessoas.py`: classe abstrata `RepositorioPessoas`, o contrato que todo repositório deve seguir (`cadastrar`, `buscar`, `listar` e `alterar`).
  - `repositorio_pessoas_memoria.py`: `RepositorioPessoasMemoria`, que guarda as pessoas em uma lista (padrão).
  - `repositorio_pessoas_mysql.py`: `RepositorioPessoasMysql`, que guarda as pessoas na tabela `pessoas` de um banco MySQL.
- `main.py`: interface em console com o usuário (menu, leitura e exibição dos dados) e escolha do repositório.

Regras:

- `pessoa.py` e `cadastro.py` não devem usar `input()` nem `print()`. Toda interação com o usuário fica em `main.py`.
- Um novo caso de uso deve ser criado como método de `CadastroPessoa` e chamado a partir de `main.py`.
- Regras de negócio (como a idade de maioridade) devem ficar em constantes em `cadastro.py`, e não repetidas no código.
- `CadastroPessoa` acessa os dados apenas pela interface `RepositorioPessoas`. Toda alteração em uma pessoa deve ser gravada chamando o repositório, para que seja persistida no banco.
- Um novo tipo de armazenamento deve ser criado em `repositorios/` como subclasse de `RepositorioPessoas`, implementando todos os seus métodos.
- Comandos SQL devem usar parâmetros (`%s`) e nunca concatenar valores informados pelo usuário.

## Ambiente de desenvolvimento

Execute os comandos a partir da raiz do projeto.

1. Crie e ative o ambiente virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   No Windows, ative com `.venv\Scripts\activate`.

2. Instale as ferramentas de qualidade:

   ```bash
   pip install pylint pytest pre-commit pymysql
   ```

3. Instale o hook do pre-commit, que roda o Pylint e o PyTest antes de cada commit:

   ```bash
   pre-commit install
   ```

4. (Opcional) Suba o MySQL com o Docker Compose, para usar o repositório MySQL e rodar os testes de integração:

   ```bash
   docker compose -f infra/compose.yaml up -d
   ```

   O repositório MySQL é configurado por variáveis de ambiente. Os valores padrão apontam para o servidor `principal` do `infra/compose.yaml`; apenas a senha precisa ser informada:

   | Variável | Padrão | Descrição |
   | --- | --- | --- |
   | `CADASTRO_REPOSITORIO` | (memória) | Use `mysql` para gravar os dados no MySQL. |
   | `MYSQL_HOST` | `127.0.0.1` | Endereço do servidor. |
   | `MYSQL_PORT` | `3307` | Porta do servidor. |
   | `MYSQL_USER` | `root` | Usuário. |
   | `MYSQL_PASSWORD` | (vazio) | Senha (no compose, a do `MYSQL_ROOT_PASSWORD`). |
   | `MYSQL_DATABASE` | `cadastro_pessoas` | Banco, criado junto com a tabela se não existir. |

   ```bash
   export MYSQL_PASSWORD=<senha do compose>
   ```

## Antes de commitar

Os comandos abaixo devem ser executados a partir da raiz do projeto.

1. Execute o Pylint e corrija todos os avisos. As regras do projeto estão no `.pylintrc`:

   ```bash
   pylint src
   ```

2. Execute os testes automatizados. A configuração fica no `pytest.ini`:

   ```bash
   pytest
   ```

3. Execute o programa e teste as opções do menu afetadas pela alteração:

   ```bash
   cd src
   python main.py
   ```

   Para testar com o MySQL, execute `CADASTRO_REPOSITORIO=mysql python main.py`.

Commits que não passam no Pylint ou nos testes são bloqueados pelo pre-commit. Mantenha o ambiente virtual ativado ao commitar, para que o hook encontre o Pylint e o PyTest.

## Testes

- Os testes ficam em `tests/`, em arquivos `test_*.py`.
- Testes são métodos em *camelCase* começando por `test` (ex.: `testBuscarPorNomeInexistente`), agrupados em classes em *PascalCase* começando por `Test`.
- Todo novo caso de uso em `CadastroPessoa` deve vir acompanhado de testes.
- Os testes do repositório MySQL (`tests/test_repositorio_mysql.py`) são de integração: usam o banco `cadastro_pessoas_teste` e são ignorados (*skipped*) quando o MySQL não está acessível. Antes de alterar um repositório, rode-os com o MySQL ligado e `MYSQL_PASSWORD` definida.

## Branches e commits

- Não faça commits diretamente na `main`. Crie uma branch para cada alteração, com nome no formato `tipo/descricao`, por exemplo `refactor/orientacao-objetos`.
- Mensagens de commit no formato `tipo: descrição`, com a descrição no imperativo e em português, por exemplo `refactor: encapsula as operações de cadastro`.
- Tipos usados:
  - `feat`: nova funcionalidade.
  - `fix`: correção de erro.
  - `refactor`: mudança no código que não altera o comportamento.
  - `style`: formatação, espaços e nomenclatura.
  - `test`: criação ou alteração de testes.
  - `docs`: documentação e docstrings.
  - `chore`: configuração e ferramentas.
