import os
os.system("cls || clear")

lista_de_numeros = []
QUANTIDADE = 6

def pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
          pares += 1
        else:
          impares += 1
    return pares, impares

print("= LISTA DE NÚMEROS =")
for i in range(QUANTIDADE):
    numero = int(input(f"Digite o {i+1}º numero: ")) 
    lista_de_numeros.append(numero)
    
pares, pares_impares = pares_impares(lista_de_numeros)

print("\n= ITENS DA LISTA =")
for i, numero in enumerate(lista_de_numeros, start = 1):
    print(f"{i}: {numero}")

print(f"\nPares: {pares}")
print(f"Ímpares: {impares}")