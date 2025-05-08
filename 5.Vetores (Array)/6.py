import os
os.system("cls || clear")

preco_total = 0
pratos_solicitados = ""
pratos = []
precos = []

os.system("cls || clear")


while True:
    print("""
    ================= MENU =================
    1 \t Picanha \t\tR$ 25,00
    2 \t Lasanha \t\tR$ 20,00
    3 \t Strogonoff \t\tR$ 18,00
    4 \t Bife acebolado \tR$ 15,00
    5 \t Pão com ovo \t\tR$ 5,00
    6 \t Feijoada     \t\tR$ 30,00
    7 \t Pizza        \t\tR$ 23,00
          
               """)

    opcao = int(input("Digite o número da prato desejada: "))


    match opcao:
        case 1:
            prato = "Picanha"
            preco = 25
            precos.append(preco)
            pratos.append(prato)
        case 2:
            prato = "Lasanha"
            preco = 20
            precos.append(preco)
            pratos.append(prato)
        case 3:
            prato = "Strogonoff"
            preco = 18
            precos.append(preco)
            pratos.append(prato)
        case 4:
            prato = "Bife acebolado"
            preco = 15
            precos.append(preco)
            pratos.append(prato)
        case 5:
            prato = "Pão com ovo"
            preco = 5
            precos.append(preco)
            pratos.append(prato)
        case _:
            print("Opção inválida. \nTente novamente... \n")
            prato = ""
            preco = 0

    preco_total = sum(precos)
    pratos_solicitados += ", " + prato if pratos_solicitados else prato
   
    mais_pedidos = input("Deseja fazer um novo pedido?\nUse 'S' or 'N' para responder: ").lower()

    if mais_pedidos == 'S':
        pratos_solicitados += 1
    if mais_pedidos == "n":
        break

print(f"Prato : {pratos_solicitados}\n seuvalor são: {precos}")
print(f"Valor total da compra: R$ {sum(precos)},00")

