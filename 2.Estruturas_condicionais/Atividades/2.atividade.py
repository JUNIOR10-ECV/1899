import os

os.system("clear")

# Utilizando condicionais aninhadas.

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

print()
print(f"Média: {media}")

if media < 7:
    print ("Reprovado")
else:
    print ("Reprovado")
 