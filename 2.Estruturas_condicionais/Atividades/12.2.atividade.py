import os

os.system("clear")
 
dia = int(input("Digite o dia da semana: "))
 
print("""
=========== DIAS DA SEMANA ===========
1  \tDomingo    
2   \tSegunda-Feira     
3   \tTerça-Feira    
4   \tQuarta-Feira      
5   \tQuinta-Feira     
6   \tSexta-Feira    
7   \tSábado
      
""")


match dia:
    case 1 | 7:
        resultado = "Fim de semana."
    case 2 | 3 | 4 | 5 | 6:
        resultado = "Dia Útil." 
    case _:
        resultado = "Opação inválida."

print()
print(f"Resultado: {resultado}")


