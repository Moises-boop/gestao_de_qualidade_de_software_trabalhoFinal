"""Sistema de cadastro de pessoas em linha de comando.

Artefato didático que serve de suporte para a disciplina de Gestão de
Qualidade de Software, curso de Ciência da Computação - UTFPR campus Medianeira.
"""

MAIORIDADE = 18
OPCAO_SAIR = 6


def ler_inteiro(mensagem):
    """Solicita um número inteiro ao usuário, repetindo até receber um valor válido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor invalido, informe um numero inteiro.")


def situacao(idade):
    """Retorna a situação da pessoa (maior ou menor de idade) de acordo com a idade."""
    if idade >= MAIORIDADE:
        return "Maior de idade"
    return "Menor de idade"


def exibir_menu():
    """Exibe o menu de opções e retorna a opção escolhida pelo usuário."""
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Avalisar cadastro")
    print("6 - Sair")
    return ler_inteiro("Escolha uma opcao: ")

def cadastrar_pessoa(nomes, idades, emails):
    """Lê nome, idade e e-mail de uma nova pessoa e os adiciona às listas."""
    nome = input("Informe o nome: ")
    idade = ler_inteiro("Informe a idade: ")
    email = input("Informe o email: ")
    nomes.append(nome)
    idades.append(idade)
    emails.append(email)
    print("Situacao: " + situacao(idade))

def exibir_pessoa(nomes, idades, emails, pos):
    """Exibe os dados e a situação da pessoa cadastrada na posição informada."""
    print("Nome: " + nomes[pos])
    print("Idade: " + str(idades[pos]))
    print("E-mail: " + emails[pos])
    print("Situacao: " + situacao(idades[pos]))

def buscar_pessoa(nomes, nome_procurado):
    """Retorna a posição de nome_procurado na lista de nomes, ou -1 se não existir."""
    pos = 0
    while pos < len(nomes):
        if nomes[pos] == nome_procurado:
            return pos
        pos = pos + 1
    return -1

def consultar_pessoa(nomes, idades, emails):
    """Solicita um nome e exibe os dados da pessoa correspondente, se cadastrada."""
    procurado = input("Nome para consultar: ")
    pos = buscar_pessoa(nomes, procurado)
    if pos == -1:
        print("Nao encontrado")
    else:
        exibir_pessoa(nomes, idades, emails, pos)

def alterar_pessoa(nomes, idades, emails):
    """Solicita um nome e substitui todos os dados da pessoa correspondente."""
    procurado = input("Nome para alterar: ")
    pos = buscar_pessoa(nomes, procurado)
    if pos == -1:
        print("Nao encontrado")
    else:
        nomes[pos] = input("Novo nome: ")
        idades[pos] = ler_inteiro("Nova idade: ")
        emails[pos] = input("Novo e-mail: ")
        print("Pessoa alterada!")
        exibir_pessoa(nomes, idades, emails, pos)

def listar_pessoas(nomes, idades, emails):
    """Exibe todas as pessoas cadastradas e o total de cadastros."""
    if len(nomes) == 0:
        print("Nenhuma pessoa cadastrada")
    pos = 0
    while pos < len(nomes):
        exibir_pessoa(nomes, idades, emails, pos)
        print("-------------------------")
        pos = pos + 1
    print("Total: " + str(len(nomes)))


def analisar_faixa_etaria(idade):
    """Exibe a faixa etária correspondente à idade."""
    if idade < 12:
        print("Faixa etaria: crianca")
    elif idade < MAIORIDADE:
        print("Faixa etaria: adolescente")
    elif idade < 60:
        print("Faixa etaria: adulto")
    else:
        print("Faixa etaria: idoso")

def analisar_contato(idade, email):
    """Exibe a situação do contato considerando a idade e o e-mail."""
    if idade >= MAIORIDADE and "@" in email:
        print("Contato: completo")
    elif idade >= MAIORIDADE:
        print("Contato: e-mail invalido")
    else:
        print("Contato: menor de idade")

def analisar_email(email):
    """Exibe o provedor do e-mail, ou indica que o e-mail é inválido."""
    if "@" not in email:
        print("E-mail invalido")
    elif email.endswith("@gmail.com"):
        print("Provedor: Gmail")
    elif email.endswith("@outlook.com"):
        print("Provedor: Outlook")
    else:
        print("Provedor: outro")

def analisar_pessoa(nomes, idades, emails):
    """Solicita um nome e exibe a análise de faixa etária, e-mail e contato."""
    procurado = input("Nome para analisar: ")
    pos = buscar_pessoa(nomes, procurado)

    if pos == -1:
        print("Pessoa nao encontrada")
    else:
        idade = idades[pos]
        email = emails[pos]

        analisar_faixa_etaria(idade)
        analisar_email(email)
        analisar_contato(idade, email)


def main():
    """Executa o laço principal do programa até o usuário escolher sair."""
    nomes = []
    idades = []
    emails = []
    acoes = {
        1: cadastrar_pessoa,
        2: consultar_pessoa,
        3: alterar_pessoa,
        4: listar_pessoas,
        5: analisar_pessoa,
    }

    opcao = 0
    while opcao != OPCAO_SAIR:
        opcao = exibir_menu()
        if opcao in acoes:
            acoes[opcao](nomes, idades, emails)
        elif opcao == OPCAO_SAIR:
            print("Saindo...")
        else:
            print("Opcao invalida")

    print("Fim do programa")


if __name__ == "__main__":
    main()
