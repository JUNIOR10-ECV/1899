import os

os.system("cls || clear")
while True:
    nota = float(input("Digite sua nota: "))  

    print()

    if nota < 1 or nota >10:
        print("Nota inválida, tente novamente.\n")
    else:
        break

print(f"Nota informada: {nota}")
