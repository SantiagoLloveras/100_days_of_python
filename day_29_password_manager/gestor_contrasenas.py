"""Logica de generacion de contrasenas y persistencia de datos."""

import string
from random import choice, randint, shuffle

ARCHIVO_DATOS = "data.txt"


def generar_contrasena():
    """Genera una contrasena aleatoria combinando letras, numeros y simbolos."""
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = "!#$%&()*+"

    letras_contrasena = [choice(letras) for _ in range(randint(8, 10))]
    simbolos_contrasena = [choice(simbolos) for _ in range(randint(2, 4))]
    numeros_contrasena = [choice(numeros) for _ in range(randint(2, 4))]

    lista_contrasena = letras_contrasena + simbolos_contrasena + numeros_contrasena
    shuffle(lista_contrasena)

    return "".join(lista_contrasena)


def guardar_contrasena(sitio_web, correo, contrasena):
    """Anade una nueva entrada (sitio, correo, contrasena) al archivo de datos."""
    with open(ARCHIVO_DATOS, "a") as archivo_datos:
        archivo_datos.write(f"{sitio_web} | {correo} | {contrasena}\n")
