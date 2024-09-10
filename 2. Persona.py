#Creame una Clase Persona.
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} {self.apellido} y tengo {self.edad} años.")

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}, {self.edad} años"
    
# Ejemplo de uso
persona1 = Persona("Juan", "Pérez", 30)
persona1.saludar()
print(persona1) # Juan Pérez, 30 años
 

