import os

os.system("clear")

primeiro_numero = float (input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero 
media = (primeiro_numero + segundo_numero) / 2

if primeiro_numero < segundo_numero: 
    maior_numero = segundo_numero
    menor_numero = primeiro_numero
else: 
    maior_numero = primeiro_numero
    menor_numero = segundo_numero

print()
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Média: {media}")

if primeiro_numero == segundo_numero: 
    print(f"Os números são iguais")
else: 
    print(f"Maior número: {maior_numero}")
    print(f"Menor número: {menor_numero}")