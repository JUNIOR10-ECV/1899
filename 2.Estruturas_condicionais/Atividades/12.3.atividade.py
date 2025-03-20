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

if dia > 1 and dia < 7:
        resultado = "Dia Útil."
elif dia == 1 or dia == 7:
        resultado = "Fima de semna." 
else:
        resultado = "Opação inválida."

print()
print(f"Resultado: {resultado}")
