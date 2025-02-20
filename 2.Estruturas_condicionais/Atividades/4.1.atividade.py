import os

os.system("clear")

login_cadastrado = "aluno"
senha_cadastrada = "123"

login = float(input("Digite seu email: "))
senha = float(input("Digite a senha: "))

if login_cadastrado == senha and senha_cadastrada == senha:
    print (f"Acesso permitido")
else:
    print (f"Acesso negado")


