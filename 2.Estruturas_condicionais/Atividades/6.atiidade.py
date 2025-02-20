import os

os.system("clear")

idade = int(input("Digite sua idade: "))

if idade <16:
    print("Não pode votar.")

elif idade <= 18:
    print("Voto opicional")

elif idade <= 65:
    print("Voto obrigatório")

else:
    print("Não é obrigado a votar")