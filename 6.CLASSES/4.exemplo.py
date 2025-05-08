import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass 
class Pessoa:
    # Variáveis = Atributos
    nome: str
    idade: int
    endereco: Endereco 

    # Função = Métodos
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"\nIdade: {self.idade}")
        print(f"\nEndereço: {self.endereco.logradouro}, número: {self.endereco.numero}")


# Aplicando característisca da classe. 
endereco1 = Endereco("Rua A", 23)
pessoa1 = Pessoa("Marta", 44, endereco1)
pessoa1.exibir_dados()

print()
endereco2 = Endereco("Rua B", 47)
pessoa2 = Pessoa("Maria", 50, endereco2)
pessoa2.exibir_dados()