import random
import json

with open("database.txt", "r") as paises_europa:
    paises_europa = json.loads(paises_europa.read())

with open("database_asia.txt", "r") as paises_asia:
    paises_asia = json.loads(paises_asia.read())

print("Bienvenido a Capital Quizz! Tienes 5 intentos para adivinar las capitales de los países que te proponemos")


def juego(modalidad):
    puntuacion = 0
    for x in range(5):
        selection = random.choice(list(modalidad.keys()))
        guess = input("¿Cuál es la capital de {0}? ".format(selection))

        capital = modalidad[selection]

        if guess.lower() == capital:
            puntuacion += 1
            print("¡Correcto!")
            continue
        if guess.lower() == "exit":
            break
        if guess.lower() != capital:
            print("¡Incorrecto!")
    print("Enhorabuena, esta vez has conseguido {0} puntos".format(puntuacion))


while True:
    mode = input("¿Quieres probar con capitales de Europa (E) o de Asia (A)? ")
    if mode.lower() == "e":
        modalidad = paises_europa
        juego(modalidad)
    if mode.lower() == "a":
        modalidad = paises_asia
        juego(modalidad)
    replay = input("¿Quieres jugar de nuevo? (Si/No) ")
    if replay.lower() == "si":
        continue
    if replay.lower() == "no":
        print("¡Gracias por jugar!")
        break
