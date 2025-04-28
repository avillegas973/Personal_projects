
#Numero secreto
import random

numero_secreto = random.randint(1, 10)
intentos = 0

while intentos < 3:
    print("Tienes 3 intentos")
    print("Intenta adivinar el número secreto entre 1 y 10")
    print("Recuerda que solo tienes 3 intentos")
    print("Si quieres salir del juego presiona 0")
    
    intento = int(input("Ingresa el número entre 1 y 10: "))
    
    if intento == 0:
        print("Saliste del juego. ¡Hasta luego!")
        break
    elif intento == numero_secreto:
        print("¡Felicidades! Has adivinado.")
        break
    else:
        print("Lo lamento, vuelve a intentarlo.")
        intentos += 1

if intentos == 3:
    print(f"Se acabaron los intentos. El número secreto era {numero_secreto}.")
# Fin del juego