import os
os.system("cls || clear")

imc = 0
def indice():

    imc = (peso) / (altura*altura)

    if imc <18.5:
        print("Abaixo do peso \n")
        print("Consulte um nutricionista \n")

    elif imc >= 18.5 and imc <=24.9:
        print("Peso normal")
        print("Mantenha hábitos saudáveis! \n")

    elif imc >= 25 and imc <=29.9:
        print("Sobrepeso \n")
        print("Considere uma dieta balanceada e atividade física \n")

    elif imc >= 30 and imc <=34.9:
        print("Obesidade grau 1 \n")
        print("Procure orientação de um profissional de saúde \n")

    elif imc >= 35 and imc <=39.9:
        print("Obesidade grau 2 \n")
        print("Consulte um médico para avaliação e orientação \n")

    elif imc >= 40:
        print("Obesidade grau 3 \n")
        print("Busque assistência médica imediatamente. \n")

    return imc

peso = float(input(f"Digite o seu peso: "))
altura = float(input(f"Digite o sua altura: "))

imc= indice()
print(f"IMC da Pessoa: {imc:.2f}")