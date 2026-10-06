"""Sistema de cadastro de pessoas em linha de comando.

Artefato didático que serve de suporte para a disciplina de Gestão de
Qualidade de Software, curso de Ciência da Computação - UTFPR campus Medianeira.
"""

from pessoa import Pessoa

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

    def cadastrarPessoa(self):
        """Lê nome, idade e e-mail de uma nova pessoa e a adiciona ao cadastro.

        Ao final, informa a situação da pessoa (maior ou menor de idade).
        """
        nome = input("Informe o nome: ")
        idade = LerInteiro("Informe a idade: ")
        email = input("Informe o email: ")

        self.cadastrar(nome, idade, email)

        print("Situacao: " + Situacao(idade))

    def consultarPessoa(self):
        """Solicita um nome e exibe os dados da pessoa correspondente, se cadastrada."""
        pessoa = self.buscarPorNome(input("Digite um nome para buscar: "))
        if pessoa is None:
            print("Pessoa nao encontrada")
            return
        ExibirPessoa(pessoa)

    def alterarPessoa(self):
        """Solicita um nome e substitui todos os dados da pessoa correspondente."""
        nome = input("Digite o nome da pessoa a alterar: ")
        if self.buscarPorNome(nome) is None:
            print("Pessoa nao encontrada")
            return

        novo_nome = input("Novo nome: ")
        nova_idade = LerInteiro("Nova idade: ")
        novo_email = input("Novo e-mail: ")

        self.alterar(nome, novo_nome, nova_idade, novo_email)

        print("Pessoa alterada!")

    def listarPessoas(self):
        """Exibe todas as pessoas cadastradas e o total de cadastros."""
        pessoas = self.listar()
        for pessoa in pessoas:
            ExibirPessoa(pessoa)
            print("-------------------------")
        print("Total de cadastros: " + str(len(pessoas)))

    def analisarPessoa(self):
        """Solicita um nome e exibe a análise de faixa etária, e-mail e contato da pessoa."""
        pessoa = self.buscarPorNome(input("Digite um nome para buscar: "))
        if pessoa is None:
            print("Pessoa nao encontrada")
            return

        print("Faixa etaria: " + AnalisarFaixaEtaria(pessoa.getIdade()))
        print("Provedor: " + AnalisarEmail(pessoa.getEmail()))
        print("Contato: " + AnalisarContato(pessoa.getIdade(), pessoa.getEmail()))

MAIORIDADE = 18
OPCAO_SAIR = 6

def LerInteiro(mensagem):
    """Solicita um número inteiro ao usuário, repetindo até receber um valor válido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor invalido, informe um numero inteiro.")

def Situacao(idade):
    """Retorna a situação da pessoa (maior ou menor de idade) de acordo com a idade."""
    if idade >= MAIORIDADE:
        return "Maior de idade"
    return "Menor de idade"

def ExibirMenu():
    """Exibe o menu de opções e retorna a opção escolhida pelo usuário."""
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Analisar cadastro")
    print("6 - Sair")
    return LerInteiro("Escolha uma opcao: ")

def ExibirPessoa(pessoa):
    """Exibe os dados e a situação da pessoa cadastrada na posição informada."""
    print("Nome: " + pessoa.getNome())
    print("Idade: " + str(pessoa.getIdade()))
    print("E-mail: " + pessoa.getEmail())
    print("Situacao: " + Situacao(pessoa.getIdade()))

def AnalisarFaixaEtaria(idade):
    """Retorna a faixa etária correspondente à idade."""
    if idade < 12:
        return "crianca"
    if idade < MAIORIDADE:
        return "adolescente"
    if idade < 60:
        return "adulto"
    return "idoso"


def AnalisarEmail(email):
    """Retorna o provedor do e-mail, ou indica que o e-mail é inválido."""
    if "@" not in email:
        return "e-mail invalido"
    if email.endswith("@gmail.com"):
        return "Gmail"
    if email.endswith("@outlook.com"):
        return "Outlook"
    return "outro"


def AnalisarContato(idade, email):
    """Retorna a situação do contato considerando a idade e a validade do e-mail."""
    if idade < MAIORIDADE:
        return "menor de idade"
    if "@" not in email:
        return "e-mail invalido"
    return "completo"


def Main():
    """Executa o laço principal do programa até o usuário escolher sair."""

    cadastro = CadastroPessoa()
    acoes = {
        1: cadastro.cadastrarPessoa,
        2: cadastro.consultarPessoa,
        3: cadastro.alterarPessoa,
        4: cadastro.listarPessoas,
        5: cadastro.analisarPessoa,
    }

    opcao = 0
    while opcao != OPCAO_SAIR:
        opcao = ExibirMenu()
        if opcao in acoes:
            acoes[opcao]()
        elif opcao == OPCAO_SAIR:
            print("Saindo...")
        else:
            print("Opcao invalida")

    print("Fim do programa")


if __name__ == "__main__":
    Main()
