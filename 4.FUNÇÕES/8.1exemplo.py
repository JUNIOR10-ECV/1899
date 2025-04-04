import os
os.system("cls || clear")

def somar(n1, n2):
    calcular = n1 + n2
    return calcular

def subtrair(n1, n2):
    calcular = n1 - n2
    return calcular

def multiplicacao (n1, n2):
    calcular = n1 * n2
    return calcular

def divisao (n1, n2):
    calcular = n1 / n2
    return calcular

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))


soma = somar(n1,n2)
subtracao = subtrair(n1,n2)
multiplicar = multiplicacao(n1,n2)
dividir = divisao(n1, 2)

print()
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicar}")
print(f"Divisão: {dividir}")