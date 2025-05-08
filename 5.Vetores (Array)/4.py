import os
os.system("cls || clear")

lista_de_numero = []
QUANTIDADE = 5 
for i in range (QUANTIDADE): 
    numero = int(input(F"Digite o {1+i}º número para lista: "))
    lista_de_numero.append(numero)

maior = max(lista_de_numero)
menor = min(lista_de_numero)

print("\n= ITENS DA LISTA =")
for i, numero in enumerate(lista_de_numero, start = 1):
    print(f"{i}: {numero}")

print()
print(f"Maior número da lista: {maior}\n")
print(f"Menor número da lista: {menor}\n")
