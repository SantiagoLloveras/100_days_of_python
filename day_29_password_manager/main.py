from tkinter import *
from tkinter import messagebox

import pyperclip

from gestor_contrasenas import generar_contrasena, guardar_contrasena

CORREO_POR_DEFECTO = "santiago@email.com"

# ---------------------------- GENERAR CONTRASENA ------------------------------- #


def generar_y_mostrar_contrasena():
    contrasena = generar_contrasena()
    entrada_contrasena.delete(0, END)
    entrada_contrasena.insert(0, contrasena)
    pyperclip.copy(contrasena)


# ---------------------------- GUARDAR CONTRASENA ------------------------------- #


def guardar():
    sitio_web = entrada_sitio_web.get()
    correo = entrada_correo.get()
    contrasena = entrada_contrasena.get()

    if not sitio_web or not correo or not contrasena:
        messagebox.showerror("Ups", "Por favor, asegúrate de no dejar ningún campo vacío")
        return

    datos_confirmados = messagebox.askokcancel(
        title=sitio_web,
        message=f"Estos son los datos introducidos:\n"
                f"Correo: {correo}\n"
                f"Contraseña: {contrasena}\n"
                f"¿Es correcto?"
    )

    if datos_confirmados:
        guardar_contrasena(sitio_web, correo, contrasena)
        entrada_sitio_web.delete(0, END)
        entrada_contrasena.delete(0, END)


# ---------------------------- INTERFAZ GRAFICA ------------------------------- #

ventana = Tk()
ventana.title("Gestor de Contraseñas")
ventana.config(padx=50, pady=50)

ventana.columnconfigure(0, weight=0)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=0)

# Logo
lienzo = Canvas(width=200, height=200, highlightthickness=0)
imagen_logo = PhotoImage(file="logo.png")
lienzo.create_image(100, 100, image=imagen_logo)
lienzo.grid(row=0, column=0, columnspan=3, pady=(0, 10))

# Etiquetas
etiqueta_sitio_web = Label(text="Sitio web")
etiqueta_sitio_web.grid(row=1, column=0, sticky="e", padx=5, pady=5)

etiqueta_correo = Label(text="Correo electrónico")
etiqueta_correo.grid(row=2, column=0, sticky="e", padx=5, pady=5)

etiqueta_contrasena = Label(text="Contraseña")
etiqueta_contrasena.grid(row=3, column=0, sticky="e", padx=5, pady=5)

# Campos de entrada
entrada_sitio_web = Entry(width=40)
entrada_sitio_web.grid(row=1, column=1, columnspan=2, sticky="ew", padx=5, pady=5)
entrada_sitio_web.focus()

entrada_correo = Entry(width=40)
entrada_correo.grid(row=2, column=1, columnspan=2, sticky="ew", padx=5, pady=5)
entrada_correo.insert(0, CORREO_POR_DEFECTO)

entrada_contrasena = Entry(width=25)
entrada_contrasena.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

# Botones
boton_generar_contrasena = Button(text="Generar contraseña", width=16, command=generar_y_mostrar_contrasena)
boton_generar_contrasena.grid(row=3, column=2, sticky="ew", padx=5, pady=5)

boton_agregar = Button(text="Agregar", command=guardar)
boton_agregar.grid(row=4, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

ventana.mainloop()
