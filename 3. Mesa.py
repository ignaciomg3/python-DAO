class Mesa:
    def __init__(self, ocupantes, nro_mesa, tipo, ubicacion):
        self.ocupantes = ocupantes
        self.nro_mesa = nro_mesa
        self.tipo = tipo
        self.ubicacion = ubicacion
        #creame un metodo para mostrar su información.
    def mostrar_info(self): 
        print(f"La mesa {self.nro_mesa} es de tipo {self.tipo}, está ubicada en {self.ubicacion} y tiene {self.ocupantes} ocupantes.")
# Ejemplo de uso

#creame una mesa.
mesa1 = Mesa(4, 1, "redonda", "el centro")
mesa1.mostrar_info()
