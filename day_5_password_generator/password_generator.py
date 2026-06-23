import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bienvenido a Password Generator!")
nro_letras = int(input("¿Cuántas letras querés en tu password?\n"))
nro_simbolos = int(input(f"¿Cuántos símbolos?\n"))
nro_numeros = int(input(f"¿Cuántos números?\n"))

password_list = []
for char in range(0, nro_letras):
    password_list.append(random.choice(letras))

for char in range(0, nro_simbolos):
    password_list.append(random.choice(simbolos))

for char in range(0, nro_numeros):
    password_list.append(random.choice(numeros))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Tu password es: {password}")

