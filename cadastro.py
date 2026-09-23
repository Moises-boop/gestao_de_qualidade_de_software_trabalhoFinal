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
    print("5 - Analisar cadastro")
    print("6 - Sair")
    return ler_inteiro("Escolha uma opcao: ")


def cadastrar_pessoa(nomes, idades, emails):
    """Lê nome, idade e e-mail de uma nova pessoa e os adiciona ao fim das listas.

    Ao final, informa a situação da pessoa (maior ou menor de idade).
    """
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
    for pos, nome in enumerate(nomes):
        if nome == nome_procurado:
            return pos
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
        return
    nomes[pos] = input("Novo nome: ")
    idades[pos] = ler_inteiro("Nova idade: ")
    emails[pos] = input("Novo e-mail: ")
    print("Pessoa alterada!")
    exibir_pessoa(nomes, idades, emails, pos)


def listar_pessoas(nomes, idades, emails):
    """Exibe todas as pessoas cadastradas e o total de cadastros."""
    if not nomes:
        print("Nenhuma pessoa cadastrada")
        return
    for pos in range(len(nomes)):
        exibir_pessoa(nomes, idades, emails, pos)
        print("-------------------------")
    print("Total: " + str(len(nomes)))


def analisar_faixa_etaria(idade):
    """Retorna a faixa etária correspondente à idade."""
    if idade < 12:
        return "crianca"
    if idade < MAIORIDADE:
        return "adolescente"
    if idade < 60:
        return "adulto"
    return "idoso"


def analisar_email(email):
    """Retorna o provedor do e-mail, ou indica que o e-mail é inválido."""
    if "@" not in email:
        return "e-mail invalido"
    if email.endswith("@gmail.com"):
        return "Gmail"
    if email.endswith("@outlook.com"):
        return "Outlook"
    return "outro"


def analisar_contato(idade, email):
    """Retorna a situação do contato considerando a idade e a validade do e-mail."""
    if idade < MAIORIDADE:
        return "menor de idade"
    if "@" not in email:
        return "e-mail invalido"
    return "completo"


def analisar_pessoa(nomes, idades, emails):
    """Solicita um nome e exibe a análise de faixa etária, e-mail e contato da pessoa."""
    procurado = input("Nome para analisar: ")
    pos = buscar_pessoa(nomes, procurado)
    if pos == -1:
        print("Pessoa nao encontrada")
        return
    idade = idades[pos]
    email = emails[pos]
    print("Faixa etaria: " + analisar_faixa_etaria(idade))
    print("Provedor: " + analisar_email(email))
    print("Contato: " + analisar_contato(idade, email))


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
