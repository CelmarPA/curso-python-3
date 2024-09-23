class Pessoa:
    def __init__(self, nome, sexo, cpf, ativo):
        self.__nome = nome
        self.__sexo = sexo
        self.__cpf = cpf
        self.__ativo = ativo

    def desativar(self):
        self.__ativo = False
        print(f'A pessoa foi desativada com sucesso!')

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


if __name__ == "__main__":
    pessoa1 = Pessoa('João', 'M', 123456, True)
    pessoa1.desativar()
    pessoa1.ativo = True
    print(pessoa1.ativo)

    # Utilizando getter e setters
    pessoa1.set_nome('José')
    print(pessoa1.get_nome())

    # Utilizando properties
    pessoa1.nome = 'Jose'
    print(pessoa1.nome)
    
