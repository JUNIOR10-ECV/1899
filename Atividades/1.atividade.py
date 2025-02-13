# Elabore um algoritimo para solicitar ao usuário um valor e escreva a mensagem : É MAIOR QUE 10!
# Se o valor lido for maior que 10, caso contráririo escrever: NÃO É MAIOR QUE 10



import os
os.system("clear") # Limpar o terminal


numero = int(input("Digite um numero: "))

if numero > 10:
    print("É maior que 10!")
else:    
    print("Não é maior que 10!")

# Exibindo dados (Saída)
    print("== Fim ==")