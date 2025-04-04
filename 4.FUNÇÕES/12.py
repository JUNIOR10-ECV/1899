import os
os.system("cls || clear")

def inflaciona(preco):
    valor = 0
    if preco < 100:
        valor = preco * 1.1
    else: 
        valor = preco * 1.2
    return valor

preco = float(input("Digite o preço do produto: R$ "))

preco_final = inflaciona(preco)

print(f"Preço final: R$ {preco_final:.2f}")