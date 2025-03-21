import os

os.system("cls || clear")

soma = 0
contador = 0

while True:
    nota = float(input(f"Digite uma nota: "))
    if nota > 0:
       soma += nota
       contador += 1
    else:
        break

media = soma / contador
print(f"\Média: {media}")