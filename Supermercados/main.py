import csv
from clases import *
def main(): 
    empresa  = Empresa()
    print(empresa)

    #punto 1
    ganancias = empresa.sumar_Ganancias()
    print(f"La ganancia total es: {ganancias}")
    #print(f"Las ganancias positivas son: {empresa.get_Positivas()} y las negativas son: {empresa.get_Negativas()}")
    empresa.get_PositivasYNegativas()
    print(f"Positivas: {empresa.positivas}")
    print(f"Negativa: {empresa.negativas}")
    #Punto 2 Cantidad de locales no rentables: 
    print(f"Mercados no Rentables: {empresa.cantidad_NO_Rentables()}")
    
    #Punto 3
    '''Local más rentable: que informe número y tipo de la sucursal 
    cuyo índice de rentabilidad sea el mayor de todos'''
    empresa.mas_rentable()



if __name__ == "__main__":
    main() 