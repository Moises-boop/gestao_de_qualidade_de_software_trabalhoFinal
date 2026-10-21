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
- `main.py`: interface em console com o usuário (menu, leitura e exibição dos dados).

Regras:

- `pessoa.py` e `cadastro.py` não devem usar `input()` nem `print()`. Toda interação com o usuário fica em `main.py`.
- Um novo caso de uso deve ser criado como método de `CadastroPessoa` e chamado a partir de `main.py`.
- Regras de negócio (como a idade de maioridade) devem ficar em constantes em `cadastro.py`, e não repetidas no código.

## Ambiente de desenvolvimento

Execute os comandos a partir da raiz do projeto.

1. Crie e ative o ambiente virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Instale as ferramentas de qualidade:

   ```bash
   pip install pylint pytest pre-commit
   ```

3. Instale o hook do pre-commit, que roda o Pylint e o PyTest antes de cada commit:

   ```bash
   pre-commit install
   ```

## Antes de commitar

Os comandos abaixo devem ser executados a partir da raiz do projeto.

1. Execute o Pylint e corrija todos os avisos. As regras do projeto estão no `.pylintrc`:

   ```bash
   pylint src/*.py
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

Commits que não passam no Pylint ou nos testes são bloqueados pelo pre-commit. Mantenha o ambiente virtual ativado ao commitar, para que o hook encontre o Pylint e o PyTest.

## Testes

- Os testes ficam em `tests/`, em arquivos `test_*.py`.
- Testes são métodos em *camelCase* começando por `test` (ex.: `testBuscarPorNomeInexistente`), agrupados em classes em *PascalCase* começando por `Test`.
- Todo novo caso de uso em `CadastroPessoa` deve vir acompanhado de testes.

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
