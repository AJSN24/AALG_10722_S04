class Perro:
    def __init__(self, nombre=""):
        self.nombre = nombre
    def muestra (self):
        print (f"Soy {self.nombre}")

p = Perro("Fido")
#p.nombre = "Fido"
p.muestra()