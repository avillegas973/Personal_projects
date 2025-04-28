
#Numero secreto
import random

numero_secreto =random.randint(1,10)

intento = int(input("Ingresa el número entre 1 y 10"))

if intento == numero_secreto:
    print("Felicidades has adivinado")
else:
    print("Lo lamento vuelve a intentarlo")