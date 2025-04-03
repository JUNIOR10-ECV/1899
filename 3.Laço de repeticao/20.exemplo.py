import os

os.system("cls || clear")

soma = 0
contador = 0

while True:
    nota = float(input(f"Digite uma nota: "))
    soma += nota
    contador +=1

    resposta = input("Deseja digitar mais uma nota?\nUse 'S' or 'N' para responder: ").lower()
    if resposta == "n":
        break
media = soma / contador

print(f"\nMèdia: {media:.2f}")
print(f"Quantidades de notas informadas: {contador}")