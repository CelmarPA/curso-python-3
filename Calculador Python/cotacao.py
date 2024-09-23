import requests
from tkinter import *


def cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cortacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cortacao_euro}
    BTC: {cotacao_btc} '''

    texto_cotacoes["text"] = texto


# Programa principal

# Cria a janela do codigo
window = Tk()
window.title('Cotação Atual das Moedas')  # Muda o titulo da janela
# window.geometry("400x400")

# Adiciona um texto na janela
texto_orientacao = Label(window, text='Clique no botão para ver as cotações das moedas!')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)  # o tkinter usar linhas e colunas para organizar os itens

# Primeiro parâmetro nome da janela, depois texto e depois a função sem o parênteses
botao = Button(window, text="Buscar cotações Dólar/Euro/BTC", command=cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

# Cria o texto para as cotações
texto_cotacoes = Label(window, text="")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

window.mainloop()  # Mantém a janela aberta
