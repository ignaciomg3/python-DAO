

"""
1) Leer el archivo mantenimientos.csv y almacenar los datos en una lista de mantenimientos.
2) Crear una instancia de la clase Maquina con los datos de la máquina.
3) Crear una instancia de la clase Mantenimiento con los datos de cada mantenimiento y agregarla a la lista de mantenimientos de la máquina.
4) Crear un Menú de opciones que contenga las siguientes opciones:
    a) Suma de gastos: que informe el total abonado por todo concepto en todos los mantenimientos registrados.
    b) Cantidad de mantenimientos caros: que informe el total de mantenimientos 
    de cualquier tipo que hayan tenido un gasto total de más de $10.000
    c) Rotura más larga: que informe la fecha y el nombre del operario del mantenimiento correctivo de mayor duración.
    cualquier otra tecla) Salir del programa.
"""


import csv
from clases import Mantenimiento, Preventivo, Correctivo, Maquina
listaMantenimientos= []

def main():
    
    leerArchivo()
    menuOpciones()


def leerArchivo():
    with open('./Primer_Parcial_Fabrica/mantenimientos.csv', mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            
            #print(row)  # Aquí puedes procesar cada fila como necesites
            id_mantenimiento, fecha, nombre, importe, res_u_horas, importe_tecnico = row
 
            # Desempaqueta los valores de la fila en variables individuales.

            #print(f"ID: {id_mantenimiento}, Fecha: {fecha}, Nombre: {nombre}, Costo: {importe}, resultado u horas: {res_u_horas}, importe_tecnico: {importe_tecnico}")
            
            if id_mantenimiento == "1":
                print("Preventivo ")
            elif id_mantenimiento == "2":
                print("Correctivo") 
            else:
                print("Error")

            iteracion = csv_reader.line_num
            print(f"Número de iteración: {iteracion}")

            # Crear una instancia de la clase importada y ejecutar alguna función
            if id_mantenimiento == '1':
                nuevoMantenimiento = Preventivo(id_mantenimiento, fecha, nombre, importe, res_u_horas, importe_tecnico)
            else:
                nuevoMantenimiento = Correctivo(id_mantenimiento, fecha, nombre, importe, res_u_horas, importe_tecnico)
            
            print("Agregar a la lista..")
            listaMantenimientos.append(nuevoMantenimiento)
            print("mantenimiento agregado")

  # Asegúrate de reemplazar 'some_module' y 'SomeClass' con los nombres correctos

def menuOpciones():
    print("**************************** MENÚ DE OPCIONES ****************************")
    print("a Suma de gastos")
    print("b Cantidad de mantenimientos caros")
    print("c Rotura más larga")
    print("* Salir del programa")

    opcion = input("Ingrese una opción: ")

    if opcion == "a":
        print("Opción a")
        sumaGastos()

    elif opcion == "b":
        print("Opción b")
        mantenimientosCaros()
    
    elif opcion == "c":
        print("Opción c")   
        roturaMasLarga()
    
    else:
        print("Saliendo del programa...")
        exit()  


    
def sumaGastos():
    total = 0
    
    
    for mantenimiento in listaMantenimientos:
        print("Importe: ", mantenimiento.importe)
        #print("Mantenimiento: ", mantenimiento)
        importeInt = int(mantenimiento.importe)
        total += importeInt
        print("total: ", total)
    print(f"El total abonado por todo concepto en todos los mantenimientos registrados es: {total}")

def mantenimientosCaros():
    total = 0
    for mantenimiento in listaMantenimientos:
        total += mantenimiento.importe
    if total > 10000:
        print(f"El total de mantenimientos de cualquier tipo que hayan tenido un gasto total de más de $10.000 es: {total}")

def roturaMasLarga():
    max_horas = 0
    for mantenimiento in listaMantenimientos:
        if isinstance(mantenimiento, Correctivo):
            if mantenimiento.horas > max_horas:
                max_horas = mantenimiento.horas
                fecha = mantenimiento.fecha
                operario = mantenimiento.operario
    print(f"La fecha y el nombre del operario del mantenimiento correctivo de mayor duración es: {fecha}, {operario}")



    
if __name__ == "__main__":
    main()


    