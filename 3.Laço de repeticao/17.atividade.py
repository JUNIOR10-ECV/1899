import os

os.system("cls || clear")
QUANTIDADE_NOTAS = 3
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("Nota inválida, tente novamente.\n")
        else:
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS

print(f'Media: {media}')

if media >=7:
    resultado = "========APROVADO========"

elif media >=5 and media <7:
    resultado ="=======RECUPERAÇÃO========"

elif media <5:
    resultado = "=======REPROVADO========"


media = soma / QUANTIDADE_NOTAS

print (f"Media: {media:.1f}:")
print (f"Resultado: {resultado}")