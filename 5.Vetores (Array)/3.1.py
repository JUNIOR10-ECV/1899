import os
os.system("cls || clear")

lista_notas = []  
quantidade_notas = 4 

for i in range(quantidade_notas):
    nota = float(input(f"Digite a {1+i}º nota: "))
    lista_notas.append(nota)

media = sum(lista_notas) / quantidade_notas

if media >=7:
    print()
    resultado = "Aprovado"
elif media >=5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print()
for nota in lista_notas:  
    print(f"Nota: {nota}")



print()
print(f"Média: {media}")
print(f"Resultado: {resultado}")