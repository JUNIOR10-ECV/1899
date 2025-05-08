import os
os.system("cls || clear")

# Criando uma lista
lista_de_compras =  []
QUANTIDADE = 3

#Solicitando dados para o usuário.
print("= LISTA DE COMPRAS =")
for i in range(QUANTIDADE):
    item = input(f"Digite o {i+1}º item para a lista de compras: ")
    lista_de_compras.append(item)

# Exibindo itens de lista de compras
print("\n= ITENS DA LISTA =")
for i, item in enumerate(lista_de_compras):
    print(f"{i}º item: {item}")
