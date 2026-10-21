"""Gerencia a interação com o usuário"""

from cadastro import CadastroPessoa

OPCAO_SAIR = 6

def LerInteiro(mensagem):
    """Solicita um número inteiro ao usuário, repetindo até receber um valor válido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor invalido, informe um numero inteiro.")

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

def ExibirPessoa(cadastro, pessoa):
    """Exibe os dados e a situação da pessoa informada."""
    print("Nome: " + pessoa.getNome())
    print("Idade: " + str(pessoa.getIdade()))
    print("E-mail: " + pessoa.getEmail())
    print("Situacao: " + cadastro.situacao(pessoa))

def CadastrarPessoa(cadastro):
    """Lê nome, idade e e-mail de uma nova pessoa e a adiciona ao cadastro.

    Ao final, informa a situação da pessoa (maior ou menor de idade).
    """
    nome = input("Informe o nome: ")
    idade = LerInteiro("Informe a idade: ")
    email = input("Informe o email: ")

    pessoa = cadastro.cadastrar(nome, idade, email)

    print("Situacao: " + cadastro.situacao(pessoa))

def ConsultarPessoa(cadastro):
    """Solicita um nome e exibe os dados da pessoa correspondente, se cadastrada."""
    pessoa = cadastro.buscarPorNome(input("Digite um nome para buscar: "))
    if pessoa is None:
        print("Pessoa nao encontrada")
        return
    ExibirPessoa(cadastro, pessoa)

def AlterarPessoa(cadastro):
    """Solicita um nome e substitui todos os dados da pessoa correspondente."""
    nome = input("Digite o nome da pessoa a alterar: ")
    if cadastro.buscarPorNome(nome) is None:
        print("Pessoa nao encontrada")
        return

    novo_nome = input("Novo nome: ")
    nova_idade = LerInteiro("Nova idade: ")
    novo_email = input("Novo e-mail: ")

    cadastro.alterar(nome, novo_nome, nova_idade, novo_email)

    print("Pessoa alterada!")

def ListarPessoas(cadastro):
    """Exibe todas as pessoas cadastradas e o total de cadastros."""
    pessoas = cadastro.listar()
    for pessoa in pessoas:
        ExibirPessoa(cadastro, pessoa)
        print("-------------------------")
    print("Total de cadastros: " + str(len(pessoas)))

def AnalisarPessoa(cadastro):
    """Solicita um nome e exibe a análise de faixa etária, e-mail e contato da pessoa."""
    pessoa = cadastro.buscarPorNome(input("Digite um nome para buscar: "))
    if pessoa is None:
        print("Pessoa nao encontrada")
        return

    print("Faixa etaria: " + cadastro.analisarFaixaEtaria(pessoa))
    print("Provedor: " + cadastro.analisarEmail(pessoa))
    print("Contato: " + cadastro.analisarContato(pessoa))


def Main():
    """Executa o laço principal do programa até o usuário escolher sair."""

    cadastro = CadastroPessoa()
    acoes = {
        1: CadastrarPessoa,
        2: ConsultarPessoa,
        3: AlterarPessoa,
        4: ListarPessoas,
        5: AnalisarPessoa,
    }

    opcao = 0
    while opcao != OPCAO_SAIR:
        opcao = ExibirMenu()
        if opcao in acoes:
            acoes[opcao](cadastro)
        elif opcao == OPCAO_SAIR:
            print("Saindo...")
        else:
            print("Opcao invalida")

    print("Fim do programa")


if __name__ == "__main__":
    Main()
