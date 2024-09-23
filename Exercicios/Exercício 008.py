# ______ Exercício 008 ______

# Escreva um programa que leia um valor em metros e o exiba em quilômetros, hectômetros,
# decâmentros, decímetros, centímentos e milímetros.

dist = float(input('Uma distância em metros: '))

km = dist / 1000
hm = dist / 100
dam = dist / 10
dm = dist * 10
cm = dist * 100
mm = dist * 1000

print(f'A medida de {dist:.1f}m corresponde a')
print(f'{km:.3f}Km')
print(f'{hm:.2f}hm')
print(f'{dam:.1f}dam')
print(f'{dm:.0f}dm')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')
