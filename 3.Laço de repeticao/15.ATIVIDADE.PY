import os

os.system("cls || clear")

login_correto = "ajr"
senha_correta = "123"

while True:
    login = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    if login == login_correto and senha == senha_correta:
        print("Bem-Vindo!")  
        break
    else:
        print("Acesso negado. \nTente novamente\n")

