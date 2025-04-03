import os

os.system("cls || clear")

numero = int(input("Digite um  número para a tabuada: "))

print(f"\nTabuada do número {numero}:")
for i in range (1, 11):
      print(f"{numero} x {i} = {i*numero}")
