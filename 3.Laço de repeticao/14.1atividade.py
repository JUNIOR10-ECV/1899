import os

os.system("cls || clear")


while True:
    nota1 = float(input("Digite sua primeira nota: "))  
    
    if nota1 < 1 or nota1 >10:
        print("Nota inválida, tente novamente.\n")
    else:
        break

while True:
    nota2 = float(input("Digite sua primeira nota: "))  
    
    if nota2 < 1 or nota2 >10:
        print("Nota inválida, tente novamente.\n")
    else:
        break

media = (nota1 + nota2) / 2
print()
print(f"Média: {media}")