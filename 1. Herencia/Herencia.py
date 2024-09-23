from abc import ABC, abstractmethod
"""
This file contains a demonstration of inheritance and abstract classes in Python.
The code defines two classes: `Persona` and `Empleado`. `Persona` is a base class that represents a person with a name and age. It has a method `saludar()` that prints a greeting message with the person's name and age.
`Empleado` is a derived class that inherits from `Persona`. It adds an additional attribute `salario` and a method `trabajar()` that prints a message indicating that the employee is working.
The code also defines an abstract class `Interface` with an abstract method `metodo_abstracto()`. This class serves as a blueprint for other classes that implement the interface. 
The class `ClaseImplementaInterface` is a concrete implementation of the `Interface` class. It overrides the `metodo_abstracto()` method and prints a message indicating that it is implementing the abstract method.
Finally, an instance of `Persona` and `Empleado` is created and their methods are called to demonstrate the functionality of the classes.
"""
from clases import Persona; 
from clases import Empleado;

# Ejemplo de uso
# Creamos una instancia de la clase Persona con el nombre "Juan" y la edad 30
persona = Persona("Juan", 30)
# Llamamos al método saludar() de la instancia de Persona para imprimir un mensaje de saludo
persona.saludar()

# Creamos una instancia de la clase Empleado con el nombre "Pedro", la edad 25 y un salario de 5000
empleado = Empleado("Pedro", 25, 5000)
# Llamamos al método saludar() de la instancia de Empleado para imprimir un mensaje de saludo
empleado.saludar()
# Llamamos al método trabajar() de la instancia de Empleado para imprimir un mensaje indicando que el empleado está trabajando
empleado.trabajar()

# Definimos una clase abstracta llamada Interface que sirve como una plantilla para otras clases que implementan la interfaz
class Interface(ABC):
    @abstractmethod
    def metodo_abstracto(self):
        pass

# Definimos una clase llamada ClaseImplementaInterface que implementa la interfaz definida en la clase Interface
class ClaseImplementaInterface(Interface):
    def metodo_abstracto(self):
        print("Implementando el método abstracto de la interfaz")

# Creamos una instancia de la clase ClaseImplementaInterface
objeto = ClaseImplementaInterface()
# Llamamos al método metodo_abstracto() de la instancia de ClaseImplementaInterface para imprimir un mensaje indicando que se está implementando el método abstracto
objeto.metodo_abstracto()
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def trabajar(self):
        print(f"{self.nombre} está trabajando.")

class Interface(ABC):
    @abstractmethod
    def metodo_abstracto(self):
        pass

class ClaseImplementaInterface(Interface):
    def metodo_abstracto(self):
        print("Implementando el método abstracto de la interfaz")

persona = Persona("Juan", 30)
persona.saludar()

empleado = Empleado("Pedro", 25, 5000)
empleado.saludar()
empleado.trabajar()

objeto = ClaseImplementaInterface()
objeto.metodo_abstracto()