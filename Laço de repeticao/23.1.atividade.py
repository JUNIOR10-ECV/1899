import os

os.system("cls || clear")


while True:

    print("""
========= MENU ===========
      
Código|\tDescrição |
        
1 - | \t Adicionar pessoa
2 - | \t Exibir resultados
3 - | \t Sair
""")
    
    opcao = int(input("Digite uma opção: "))

    match opcao:
        case 1:
            input("Idade: ")
            input("Sexo: ")
            input("Salario: ")

            os.system("cls || clear")
        case 2:

        case 3:

        case _:
            os.system("cls || clear")
