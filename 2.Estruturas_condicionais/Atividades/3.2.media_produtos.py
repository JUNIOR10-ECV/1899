import os

os.system("clear")

# Utilizando condicionais aninhadas.
primeiro_numero = float (input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero 
media = (primeiro_numero + segundo_numero) / 2

maior_numero = max(primeiro_numero, segundo_numero)
menor_numero = min(primeiro_numero, segundo_numero)

print()
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Média: {media}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")