# 1 - Limpando o Terminal
import os

os.system("clear")

# 2 - Cadstrando o Login e senha
login_cadastrado = "aluno"
senha_cadastrada = "123"
# Solicitando dados para o usúario
login = input("Digite seu email: ")
senha = input("Digite a senha: ")

# 4 - Verificando os dados cadastrados com os dados informados
# pelo usúario. 
if login_cadastrado == senha and senha_cadastrada == senha:
    print (f"Acesso permitido")
else:
    print (f"Acesso negado")


