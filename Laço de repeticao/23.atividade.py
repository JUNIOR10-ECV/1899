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

    contador = 0
    salario2 = 0
    idade = 0
    maior_idade = 0
    menor_idade = 0


    codigo = int(input("Digite o Código: "))
    match codigo:
        case 1:
            nome = input("Nome da pessoa: ")
            idade = int(input(idade))
            idade2 +=2
            salario = int(input("Salario da pessoa"))
            salario2 += salario
            contador += 1
        
        case 3:
            break

maior_idade = max(idade)
meor_idade = min(idade)
