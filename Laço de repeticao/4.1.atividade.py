import os
import time

os.system("cls || clear")

print("Comtagem de 100 até 120 \nApenas pares.")
print()
for i in range(100, 121, 2):
    print(f"Valor da variável i: {i}")
    print()
    time.sleep(0.1) 

print("ACABOU.")