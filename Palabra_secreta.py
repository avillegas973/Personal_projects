
#Palabra secreta
import random

palabras = ["python", "programacion", "secreto", "reto", "codigo", "algoritmo", "computadora", "variable", "bucle", "condicional"]

palabra_secreta = random.choice(palabras)

intentos = 0

while intentos < 5:
    print(f"Tienes {5 - intentos} intentos restantes.")
    print(f"La palabra secreta tiene {len(palabra_secreta)} letras.")
    print("Si quieres salir del juego escribe 0.")
    
    intento = input("Ingresa tu intento: ")
    
    if intento == "0":
        print("Saliste del juego. ¡Hasta luego!")
        break
    elif intento == palabra_secreta:
        print("¡Felicidades! Has adivinado la palabra secreta.")
        break
    else:
        print("Lo lamento, vuelve a intentarlo.")
        intentos += 1

if intentos == 5:
    print(f"Se acabaron los intentos. La palabra secreta era '{palabra_secreta}'.")
# Fin del juego


