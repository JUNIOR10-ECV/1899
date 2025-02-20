import os

os.system("clear")
55
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

if primeiro_numero == segundo_numero:
    print(f"Os números são iguais")
else: 
    print(f"Miaor número: {maior_numero}")
    print(f"Maior número: {menor_numero}")