import os

os.system("clear")


print("""
=========== DIAS DA SEMANA ===========
| 1 | Segunda-Feeira\t\
      
| 2 | Terça-Feira\t\
      
| 3 | Quarta-Feira\t\
      
| 4 | Quinta-Feira\t\
      
| 5 | Sexta-Feira\t\
      
| 6 | Sábado\t\
      
| 7 | Domingo\t\
      
""")

opcao = int(input("Digite o dia da semana: "))

match opcao:
    case 1:
        dia = "Sgunda-Feira"
        dia_da_seman = "Útil"
    case 2:
        dia = "Terça-Feira"
        dia_da_seman = "Útil"
    case 3:
        dia = "Quarta-Feira"
        dia_da_seman = "Útil"
    case 4:
        dia = "Quinta-Feira"
        dia_da_seman = "Útil"
    case 5:
        dia = "Sexta-Feira"
        dia_da_seman = "Útil"
    case 6:
        dia = "Sabado"
        dia_da_seman = "Final de Semana"
    case 7:
        dia = "Domingo"
        dia_da_seman = "Final de Semana"
    case _:
        dia = "Opção invalida"
        dia_da_seman = "Invalidoo"

print()
print(f"Dia: {dia}")
print(f"Dia da semana: {dia_da_seman:.2f}")

