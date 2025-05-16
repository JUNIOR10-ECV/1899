import os
from dataclasses import dataclass

os.system('cls || clear')

@dataclass
class Paciente:
    nome: str
    data_nascimento: float
    rg: int
    cpf: int

lista_usuarios= []

for i in range(5):
    print("Digite os dados do pacienete: ")
    paciente = Paciente(
        nome= input("Nome: "),
        idade= int(input("Idade: "))
    )
    lista_usuarios.append(paciente)
    print()

nome_arquivo = "dados_pacientes.csv"

print("Salvando dados no arquivo.")
with open(nome_arquivo, "a") as arquivo_pacientes:
    for paciente in lista_usuarios:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade} \n")

print("Salvo com sucesso.")

print("\nAcessando dados em arquivos.")
try:
    with open(nome_arquivo, "r") as arquivos_pacientes:
        linhas = arquivo_pacientes.readlines()
        for linha in linhas:
            print(f"- {linha.strip()}")
except FileNotFoundError:
    print("O arquivo nãofoi encontrado.")