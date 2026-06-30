class Controles:

    def __init__(self):
        self.teclas_presionadas = {
            "Up": False,
            "Down": False,
            "w": False,
            "s": False,
        }

    def presionar_tecla(self, key):
        self.teclas_presionadas[key] = True

    def liberar_tecla(self, key):
        self.teclas_presionadas[key] = False
