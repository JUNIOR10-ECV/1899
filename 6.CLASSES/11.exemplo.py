import os
from dataclasses import dataclass

os.system('cls || clear')

@dataclass
class Usuario:
    nome: str
    data_nascimento: float
    rg: int
    cpf: int

lista_de_usuarios = []

for i in range(5):
    print("Digite os dados do pacienete: ")
    usuario = Usuario(
        nome= input("Nome: "),
        data_nascimento= float(input("Data de nascimento: ")),
        rg= int(input("RG: ")),
        cpf= int(input("CPF: "))
    )
    lista_de_usuarios.append(usuario)
    print()

nome_arquivo = "dados_pacientes.csv"

print("Salvando dados no arquivo.")
with open(nome_arquivo, "a") as arquivo_usuarios:
    for usuario in lista_de_usuarios:
        arquivo_usuarios.write(f"{usuario.nome}, {usuario.data_de_nascimento}, {usuario.rg}, {usuario.cpf} \n")

print("Salvo com sucesso.")

print("\nAcessando dados em arquivos.")
try:
    with open(nome_arquivo, "r") as arquivos_pacientes:
        linhas = arquivo_usuarios.readlines()
        for linha in linhas:
            print(f"- {linha.strip()}")
except FileNotFoundError:
    print("O arquivo nãofoi encontrado.")

