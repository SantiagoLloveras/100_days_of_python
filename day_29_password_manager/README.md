# Gestor de Contraseñas

Aplicación de escritorio con interfaz gráfica (Tkinter) para generar contraseñas
seguras y guardarlas junto al sitio web y el correo/usuario asociado.

## Funcionalidad

- Genera una contraseña aleatoria (letras, números y símbolos) y la copia
  automáticamente al portapapeles.
- Guarda el sitio web, el correo/usuario y la contraseña en `data.txt`.
- Valida que no se guarden campos vacíos y pide confirmación antes de guardar.

## Estructura del proyecto

```
password_manager/
├── main.py                 # Interfaz grafica (Tkinter)
├── gestor_contrasenas.py   # Logica de generacion y guardado de contrasenas
├── logo.png                # Logo mostrado en la interfaz
└── requirements.txt
```

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

1. Escribe el sitio web y el correo/usuario.
2. Pulsa **Generar contraseña** (o escribe una manualmente).
3. Pulsa **Agregar** y confirma los datos para guardarlos en `data.txt`.
