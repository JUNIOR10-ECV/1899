import os
import time

os.system("cls || clear")

print("Ímpares de 1 até 20:")
for i in range(1, 21):
    if i % 2 == 1:
        print(f"Número: {i}")
        time.sleep(0.5)