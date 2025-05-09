import os
from dataclasses import dataclass
os.system('cls || clear')

lista_Autor = [] #Criando uma lista para adicionar clientes.
QUANTIDADES_AUTOR = 2

@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor


for i in range(QUANTIDADES_AUTOR):
    livro = Livro(
        titulo = input('Titulo:'), #Não esqueça da virgula.
        ano = input('Ano:'),
        autor=Autor(
            nome=input('Autor:'), #no último nao tem virgula.
            biografia=input('biografia: ')
            )
    )
    lista_Autor.append(livro) # Adicionando um cliente na lista.
    print()

for livro in lista_Autor: # Mostra os dados por elementos na lista.
    print(f"Título:{livro.titulo} ")
    print(f"Ano:{livro.ano} ")
    print(f"Autor:{livro.autor.nome} ")
print()