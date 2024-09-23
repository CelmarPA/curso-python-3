class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def mudar_canal(self, botao):
        if botao == '+':
            print(f'Aumentar o Canal')
        elif botao == '-':
            print(f'Diminuir o Canal')

    def alterar_volume(self, botao):
        if botao == '+':
            print(f'Aumentar o volume')
        elif botao == '-':
            print(f'Diminuir o volume')

    def abrir_netflix(self):
        print(f'Abrindo Netflix...')

    def desligar_tv(self):
        print(f'Desligando a tv...')


controle_remoto = ControleRemoto('preto', '10cm', '2cm', '2cm')
print(controle_remoto.cor)
controle_remoto.mudar_canal('+')

controle_remoto2 = ControleRemoto('cinza', '10cm', '2cm', '2cm')
print(controle_remoto2.cor)
controle_remoto.mudar_canal('-')
