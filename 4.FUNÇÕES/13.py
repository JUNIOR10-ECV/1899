import os
from datetime import datetime
os.system("cls || clear")

def calcular_idade(ano_nascimento):
    return datetime.now().year -ano_nascimento
ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade = calcular_idade(ano_nascimento)

print(f"Sua Idade é: {idade}")