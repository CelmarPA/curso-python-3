""" Exercício 01 - Crie um sistema de gerenciamento de funcionários para uma empresa. Cada funcionário possui
    um nome, um salário base e um cargo específico. Existem dois tipos de funcionários: normais e gerentes.

    1. Crie uma classe base chamada Funcionario com os seguintes atributos privados:
        _nome (string): Nome do funcionário.
        _salario_base (float): Salário base do funcionário.

        A classe deve ter um método chamado calcular_salario que retorna o salário total do funcionário. Este método
        deve ser implementado pelas subclasses.

    2. Crie uma subclasse chamada FuncionarioNormal, que herda da classe Funcionario. Esta subclasse deve ter um método
    adicional chamado apresentar que exibe uma mensagem informando o nome, cargo e salário total do funcionário normal.

    3. Crie uma subclasse chamada Gerente, que também herda da classe Funcionario. Um gerente tem um bônus adicional ao
    salário base. Adicione um atributo privado _bonus (float) à classe Gerente e modifique o método calcular_salario
    para incluir o bônus.

    4. No programa principal, crie pelo menos um objeto de cada classe (FuncionarioNormal e Gerente), defina valores
    para os atributos e exiba a apresentação de cada funcionário.

    Observações: Considere que o bônus para o gerente é 10% do salário base. Utilize o encapsulamento adequado para os
    atributos privados. """

# Importação de pacotes
from exercicios.ex001.lib. classes import *

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{"Sistema de Gerenciamento de Funcionários":^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Programa principal

# Funcionário Normal
funcionario_normal = FuncionarioNormal('João', 5000)
funcionario_normal.apresentar()

# Gerente
gerente = Gerente('Maria', 8000, 10)
gerente.apresentar()
