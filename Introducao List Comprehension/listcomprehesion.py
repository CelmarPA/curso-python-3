# Cria uma lista de quadrados dos números de 0 a 9:
squares = [x**2 for x in range(10)]

print(squares)

# Cria uma lista apenas com os números pares de 0 a 9:
even_numbers = [x for x in range(10) if x % 2 == 0]

print(even_numbers)

# Converte cada letra em uma string para maiúscula:
original = ['abc', 'def', 'ghi']
uppercase = [char.upper() for word in original for char in word]

print(uppercase)

# Filtra palavras que têm mais de três letras:
words = ['apple', 'banana', 'grape', 'kiwi', 'hi', 'you', 'buy', 'car']
filtered_words = [word for word in words if len(word) > 3]

print(filtered_words)
