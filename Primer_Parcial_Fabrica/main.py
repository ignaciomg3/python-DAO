

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
from clases import *
def main():

    ''' 
    - Suma de gastos: que informe el total abonado por todo concepto en todos los mantenimientos registrados.
    
    - Cantidad de mantenimientos caros: que informe el total de mantenimientos de cualquier 
    tipo que hayan tenido un gasto total de más de  $10.000
     
     - Rotura más larga: que informe la fecha y el nombre del operario del mantenimiento correctivo de mayor duración
    '''
    m = Maquina()
    m.cargar_datos()
    m.__str__()
    print(m)
    
    #PUNTO 1
    suma = m.suma_Gastos()
    print(f"la suma total de los gastos es: {suma}")
    
    #PUNTO 2
    print (f"la cantidad de mantenimientos caros son: {m.cant_Mant_Caros()}")

    #PUNTO 3
    mant = m.rotura_Mas_Larga()
    print(f"La rotura mas larga es: {mant.fecha} el operario es: {mant.operario} \n la cantidad de horas parada es: {mant.horasParada}")
    
    

if __name__ == "__main__":
    main()