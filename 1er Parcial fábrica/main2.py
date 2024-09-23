import csv;


from clases import Mantenimiento;
mantenimientos = []

def cargar_mantenimientos():
    # Define la función cargar_mantenimientos que no recibe parámetros y no retorna nada.
    
    with open('mantenimientos.csv', mode='r', encoding='utf-8', newline='') as file:
        # Abre el archivo 'mantenimientos.csv' en modo lectura ('r') con codificación 'utf-8'.
        # El bloque 'with' asegura que el archivo se cierre automáticamente después de ser usado.
        
        csv_reader = csv.reader(file,delimiter=',')
        # Crea un lector de CSV que iterará sobre las líneas del archivo.
        
        for row in csv_reader:
            # Itera sobre cada fila del archivo CSV.
            
            id_mantenimiento, fecha, nombre, costo, id_tecnico, horas = row
            # Desempaqueta los valores de la fila en variables individuales.

            print(f"ID: {id_mantenimiento}, Fecha: {fecha}, Nombre: {nombre}, Costo: {costo}, ID Técnico: {id_tecnico}, Horas: {horas}")
            
            mantenimiento = Mantenimiento(id_mantenimiento, fecha, nombre, costo, id_tecnico, horas)
            # Crea una instancia de la clase Mantenimiento con los valores desempaquetados.
            
            mantenimientos.append(mantenimiento)
            # Agrega la instancia de Mantenimiento a la lista mantenimientos.


def main():
    cargar_mantenimientos()

if __name__ == "__main__":
    main()  
# Define la función main que no recibe parámetros y no retorna nada.
"""
Lee un archivo CSV llamado 'mantenimientos.vsc' y 
imprime cada fila en la consola.
El archivo se abre en modo de lectura ('r') con codificación 'utf-8'.
Utiliza el módulo csv para leer el contenido del archivo.
"""
