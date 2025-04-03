import os
os.system("cls || clear")

def verificar (num):
    if num % 2 == 0:
        print("O numero é par.")
    else:
        print("O numero é impar")

print("Verificando se um número é par ou impar.")
num = int(input("Digite um número: "))
verificar(num)