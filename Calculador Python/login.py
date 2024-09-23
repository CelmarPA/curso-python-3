from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')  # Define o tema
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha '), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

#  Janela
window = sg.Window('Tela de Login', layout)

# Ler os eventos
while True:
    eventos, valores = window.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'celmar' and valores['senha'] == '123456':
            print(f'Bem vindo ao Python')
            