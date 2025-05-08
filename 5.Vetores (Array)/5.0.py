import os
os.system("cls || clear")

lista_de_numeros = []
pares = 0
impares = 0
QUANTIDADE = 6

print("= LISTA DE NÚMEROS =")
for i in range(QUANTIDADE):
    numero = int(input(f"Digite o {i+1}º numero:")) 

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n= ITENS DA LISTA =")
for i, numero in enumerate(lista_de_numeros, start = 1):
    print(f"{i}: {numero}")

print(f"\nPares: {pares}")
print(f"Ímpares: {impares}")