import os
from dataclasses import dataclass
os.system('cls || clear')

@dataclass
class Carros:
    marca:str
    modelo: str
    categoria: str
    preco: float

lista_carros = []
QUANTIDADES_CARROS = 2

print("Informe os dados do carros:")
for i in range(QUANTIDADES_CARROS):
    carros = Carros(  
        marca = input("Marca: "), 
        modelo = input("Modelo: "),
        categoria = input("Categoria: "),
        preco = input("Preço: ")
    )
    lista_carros.append(Carros) # Adicionando um cliente na lista. 
    print()

print('\n= Exibindo dados Carros =')
for carros in lista_carros: # Mostra os dados por elementos na lista.
    print(f"Marca:{carros.marca} ")
    print(f"Modelo:{carros.modelo} ")
    print(f"Categoria:{carros.categoria} ")
    print(f"Preço:{carros.preco} ")
    print()

print("= Salvando os dados dos carros =")
nome_arquivos = "carros.txt"

with open(nome_arquivos, "a") as arquivo:
    for carros in lista_carros:
        arquivo.write(f"{carros.marca}, {carros.modelo}, {carros.categoria}, {carros.preco}\n")
print("\nSalvo com sucesso!")