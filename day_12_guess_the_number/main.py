from art import logo
import random

NIVEL_FACIL_INTENTOS = 10
NIVEL_DIFICIL_INTENTOS = 5

print(logo + "\n")

# 1. Mensaje bienvenida y elegir dificultad
print("Bienvenido al juego 'Adivina el Número!'")
dificultad = int(input("Elegí la dificultad. Escribí '1' para fácil o '2' para dificil: "))
print()
if dificultad == 1:
    intentos = NIVEL_FACIL_INTENTOS
else:
    intentos = NIVEL_DIFICIL_INTENTOS

numero_a_adivinar = random.randrange(101)

print(f"Estoy pensando en un número que está entre 1 y 100. Tenés {intentos} intentos para adivinarlo.")


# 2. Input numero elegido, chequeo, si adivina pasa, si no resta vida y continua
gano = False
continuar = True

def actualizar_intentos():
    global intentos
    global continuar
    intentos -=1
    if intentos == 0:
        continuar = False
    else:
        print(f"Te quedan {intentos} intentos para adivinar el número.\nIntentá de nuevo.\n")

while continuar:
    numero_elegido = int(input("Elegí un número: "))
    if numero_elegido == numero_a_adivinar:
        gano = True
        continuar = False
    elif numero_elegido > numero_a_adivinar:
        print("Muy alto!")
        actualizar_intentos()
    else:
        print("Muy bajo!")
        actualizar_intentos()

if not gano:
    print("Te quedaste sin intentos!")
else:
    print("GANASTE!!! Bien hecho!!!")
