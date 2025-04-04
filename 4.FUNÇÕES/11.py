import os
os.system("cls || clear")

def cconverta_centimetros(numero):
    return numero * 100

numero = float(input("Digite o valor em metros: "))

centimetros = cconverta_centimetros(numero)

print(f"Coverta {numero} m em centímetros é: {centimetros} cm.")