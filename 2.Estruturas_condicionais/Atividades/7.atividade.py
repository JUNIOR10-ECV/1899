# 1 - Limpando o terminal

import os

os.system("clear")

# 2 - Solicitando dados para o usuário.
primeiro_numero= int(input("Digite o primeiro número: "))

segundo_numero = int(input("Digite o segundo número: "))

# 3 - Verificando o maior e o menor.
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

# 4 - Exibindo resultados.
print()
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
