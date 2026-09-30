class Pessoa:
    """Definição da classe pessoa"""
    def __init__(self, nome, idade, email):
        """Define o contrato da classe"""
        self.__nome = nome
        self.__idade = idade 
        self.__email = email
    
    def getNome(self):
        """Retorna o nome da pessoa"""
        return self.__nome

    def getIdade(self):
        """Retorna a idade da pessoa"""
        return self.__idade
    
    def getEmail(self):
        """Retorna o email da pessoa"""
        return self.__email

    def setNome(self, nome):
        """Altera o nome da pessoa cadastrada com o nome passado como argumento"""
        self.__nome = nome

    def setIdade(self, idade):
        """Altera a idade da pessoa cadastrada com a idade passada como argumento"""
        self.__idade = idade

    def setEmail(self, email):
        """Altera o email da pessoa cadastrada com o email passado como argumento"""
        self.__email = email