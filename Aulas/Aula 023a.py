try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou!')
except ZeroDivisionError:
    print(f'Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print(f'O usuário preferii não informa os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultador é {r:.1f}')
finally:
    print(f'Volte sempre muito obrigado!')

"""try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print(f'Infelizmente tivemos um problema :(!')
else:
    print(f'O resultador é {r:.1f}')
finally:
    print(f'Volte sempre muito obrigado!')"""
