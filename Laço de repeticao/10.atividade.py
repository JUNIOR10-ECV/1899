import os

os.system("cls || clear")

soma = 0

for i in range(4):
    numero = int(input("Digite o número da sua nota: "))
    soma += numero

print (f"A soma tota é {soma}")

media = (soma)/4

print (f"A mdia total é  {media}")
