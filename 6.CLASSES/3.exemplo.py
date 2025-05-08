import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = Pessoa(
    nome=input("Digite o nome: "),
    idade=int(input("Digite a idade: ")),
    peso=float(input("Digite o peso: ")),
    altura=float(input("Digite a altura: "))
    )

print()

pessoa2 = Pessoa(
    nome=input("Digite o nome: "),
    idade=int(input("Digite a idade: ")),
    peso=float(input("Digite o peso: ")),
    altura=float(input("Digite a altura: "))
    )

    
print(f"\nNome: {pessoa1.nome}, idade: {pessoa1.idade} anos. ")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade} anos. ")