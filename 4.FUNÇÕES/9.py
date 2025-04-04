import os
os.system("cls || clear")

def calcular_media(n1, n2):
    soma = n1 + n2
    media = soma / 2
    return media

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

media = calcular_media(n1, n2)

print(f"Média: {media}")