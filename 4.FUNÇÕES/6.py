import os
os.system("cls || clear")

def verificar (num):
    if num > 0:
        print("O número é positivo.")

    elif num == 0:
        print("Número neutro")
    else:
        print("O número é negativo")

print("Verificando se o número é negativo ou positivo.")
num = int(input("Digite um número: "))
verificar(num)