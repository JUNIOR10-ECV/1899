import os

os.system("cls || clear")

# Exemplo de uso do laço de repetição while.
idade = int(input("Digite su idad: "))

while idade < 18:
    print("Não autorizado. \nSomente maiores de 18.\n")
    idade = int(input("Digite sua idade"))  

print("Acesso permitido")
print("Fim.")