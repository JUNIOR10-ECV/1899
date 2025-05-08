import os
os.system("cls || clear")

# Função para calcular média.
def calcular_media(lista):
    #sum(lista) irá somar os valores na lista.
    #len(lista) irá mostrar a quantidade de valores na lista.
    media = sum(lista) / len(lista)
    return media

lista_notas = [] # Criando uma lista.
QUANTIDADE_NOTAS = 2 # Criando uma constante.

# Solicitando dados para o usúario.
for i in range(QUANTIDADE_NOTAS):
        nota = float(input(f'Digite a {I+1}ª NOTA: '))

# Chamada a função para calcular a média.
# Enviando a lista de notas como parâmetro.
# Inserido na variável 'media' o cálculo retornando pela função.
media = calcular_media(lista_notas)

# Exibindo a média.
print(f"\nMéia: {media}")

