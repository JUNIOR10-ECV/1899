import os

os.system("cls || clear")

pares = 0
impares = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares +=1
    else:
        impares += 1

print()
print(f"Ímpares: {impares}" )
print(f"Par: {pares} ")        