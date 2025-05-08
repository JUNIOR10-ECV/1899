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
    email: str
    endereco: Endereco 
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"\nEmail: {self.email}")
        print(f"\nEndereço: {self.endereco.logradouro}, número: {self.endereco.numero}")

endereco1 = Endereco("Rua A", 23)
pessoa1 = Pessoa("Marta", "Neymar@gmail.com", endereco1)
pessoa1.exibir_dados()

print()
endereco2 = Endereco("Rua B", 47)
pessoa2 = Pessoa("Maria","CR7@gmai.com", endereco2)
pessoa2.exibir_dados()