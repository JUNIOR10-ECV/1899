import os

os.system("clear")

n1 = int(input("Digite o primeiro número: "))
operacao = input("Digite a operção desejada: ")
n2 = int(input("Digite o segundo número: "))

match operacao:
    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
    case "*":
        resultado = n1 * n2
    case "/":
        resultado = n1 / n2
    case _:
        print("Opção invalida.")

print()
print(f"Primeiro número: {n1} ")
print(f"Operação: {operacao} ")
print(f"Segundo número {n2}")
print(f"Resultado: {resultado}")