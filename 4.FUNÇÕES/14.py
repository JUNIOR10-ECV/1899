import os
os.system("cls || clear")

soma = 0

def calcular(soma):
    return soma / 3

for i in range(3):
    nota = float(input(f"Digite sua {1+i}º nota: "))
    print()
    soma += nota

media = calcular(soma)
print(f"Media: {media:.2f}")