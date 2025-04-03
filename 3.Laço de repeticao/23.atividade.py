import os
import time

os.system("cls || clear")
contador = 0
soma_salario = 0 
maior_idade = 0
menor_idade = 0
mulheres5k = 0

while True:
    print("""
========= MENU ===========
      
Código|\tDescrição |
        
1 - | \t Adicionar pessoa
2 - | \t Exibir resultados
3 - | \t Sair
""")


    opcao = int(input("Digite o Código: "))

    match opcao:
        case 1:
            idade = int(input("Digite a idade: "))
            sexo = input("Iforme o sexo com 'M' ou 'F': " )
            salario = float(input("Informe o sálario: "))
            contador += 1
            soma_salario += salario
            
            if idade > maior_idade:
                maior_idade = idade

            if idade < menor_idade:
                menor_idade = idade

            if sexo == "F" and salario >= 5000:
                mulheres5k  += 1

            os.system("cls || clear")
        case 2:
            if contador > 0:
                medida_salario_grupo = soma_salario / contador
                print("\n= Exibido resultados = ")
                print(f"Média de salario do grupo: {medida_salario_grupo}")
                print(f"Maior idade do grupo: {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Quantidade mulheres com sálaio a parti de 5 mil: {mulheres5k}")
            else: 
                print("Não existem dados para exibir.")

            time.sleep(3)
            os.system("cls || clear")
        case 3:
            print("\nFim do programa.")
            break
        case _:
            print("\nOpção inválida.")
            time.sleep(3)
            os.system("cls || clear")



    
    