import csv

"""
1) Leer el archivo mantenimientos.csv y almacenar los datos en una lista de mantenimientos.
2) Crear una instancia de la clase Maquina con los datos de la máquina.
3) Crear una instancia de la clase Mantenimiento con los datos de cada mantenimiento y agregarla a la lista de mantenimientos de la máquina.
"""

  # Asegúrate de reemplazar 'some_module' y 'SomeClass' con los nombres correctos
from clases import Mantenimiento, Preventivo, Correctivo, Maquina;

def main():
    # Leer el archivo CSV
    with open('mantenimientos.csv', mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)  # Aquí puedes procesar cada fila como necesites

    # Crear una instancia de la clase importada y ejecutar alguna función
    instance = Mantenimiento()
    instance.mostrar()  # Asegúrate de reemplazar 'some_method' con el método correcto


def leer_mantenimientos(archivo):
    mantenimientos = []
    with open(archivo, newline='') as csvfile:
        lector = csv.reader(csvfile)
        for fila in lector:
            mantenimientos.append(fila)  # Cada fila es una lista de elementos
    return mantenimientos


if __name__ == "__main__":
    main()