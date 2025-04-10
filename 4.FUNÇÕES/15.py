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

if media >=7:
    print()
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print(f"Média: {media:.2f}")
print(f"Resultado: {resultado}")

