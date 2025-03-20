import os

os.system("clear")
 
mes = int(input("Digite um número para o mês do ano: "))
 


match mes:
    case 1:
        resutado = print("Janeiro")
    case 2:
        resutado = print("Fevereiro")
    case 3:
        resultado = print("Março")
    case 4:
        resultado = print("Abril")
    case 5:
        resultado = print("Maio")
    case 6:
        resultado = print("Junho")
    case 7:
        resultado = print("Julho")
    case 8:
        resultado = print("Agosto")
    case 9: 
        resultado = print("Setembro")
    case 10: 
        resultado = print("Outubro")
    case 11: 
        resultado = print("Novembro")
    case 12:
        resultado = print("Dezembro")
    case _:
        resultado = "Opçaõ ivalida"

print()
print(f"Resultado: {resultado}")
