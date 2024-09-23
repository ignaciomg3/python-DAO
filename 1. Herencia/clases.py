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
 
 

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Salario: {self.salario}')
        # Persona.py
        class Persona:
            def __init__(self, nombre, edad):
                self.nombre = nombre
                self.edad = edad

            def mostrar_informacion(self):
                print(f'Nombre: {self.nombre}, Edad: {self.edad}')

 

        

