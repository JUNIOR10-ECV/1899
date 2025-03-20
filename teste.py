import os

os.system("clear")

nome = str(input("Digite seu nome: "))
sexo = str(input("Digite seu sexo: ")).lower()

match sexo:
    case "f":
        