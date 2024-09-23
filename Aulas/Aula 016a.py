lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são imutáveis

pessoa = ('Gustavo', 39, 'M', 99.88)
del pessoa  # É imutável, mas pode ser completamente deletada
print(pessoa)

'''pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a  # Une as duas tuplas em ordem
print(c)
print(c.count(4))  # Conta quantos tem
print(c.index(5, 1))  # Deslocamento '''

'''print(sorted(lanche))  # Mostra a tupla lanche em ordem, não muda a tupla'''

'''for count in range(len(lanche)):
    print(f'Eu vou comer {lanche[count]} na posição {count}.')'''

'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer  {comida} na posição {pos}.')'''

'''for count in range(0, len(lanche)):
    print(lanche[count])'''

'''for comida in lanche:
    print(f'Eu comer {comida}!')
print(f'Comi muito!!!')'''
