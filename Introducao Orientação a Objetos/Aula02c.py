# Criar uma classe para clientes da Netflix

class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception(f'Plano inválido!')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print(f'Plano inválido!')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}')
        elif self.plano == 'basic' and  plano_filme == 'premium':
            print(f'Faça upgrade para premium para ver esse filme')
        else:
            print(f'Plano inválido!')


cliente = Cliente('Lira', 'lira@gmail.com', 'basic')
print(cliente.nome)
print(cliente.plano)
cliente.ver_filme('Harry Potter', 'premium')

# Botão de mudar plano
cliente.mudar_plano('premium')
print(cliente.plano)
cliente.ver_filme('Harry Potter', 'premium')
