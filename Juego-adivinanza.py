

import random


numero_secreto = random.randint(1, 101)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("¡Te damos la bienvenida al juego de adivinar el número secreto!")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("¡Juego terminado! no lograste adivinar el número secreto")
        break

    entrada = input("Ingresar un número del 1 al 100: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("¡Felicidades, adivinaste el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El número secreto es mayor al ingresado")
    else:
        print("El número secreto es menor al ingresado")

    cant_intentos += 1

