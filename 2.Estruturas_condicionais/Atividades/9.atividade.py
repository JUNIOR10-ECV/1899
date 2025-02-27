import os

os.system("clear")

numero_maça = int(input("Quantas maçãs você quer: "))

print(f"Número de maçãs: {numero_maça} ")

if numero_maça < 12:
    numero_maça = numero_maça * 1.30
    print(f"Valor total R$: {numero_maça} ")

else:
    numero_maça= numero_maça * 1.0
    print(f"Valor total R$: {numero_maça:.2f}")

