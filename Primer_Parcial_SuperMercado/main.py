import csv
from clases import Sucursal, Hiper, Supermercado, Mini

listaSucursales = []


def main():

    leerArchivo()
    
    sumaGanancia()
    localesNoRentables()
    localMasRentable()



def leerArchivo():

    #abrir el archivo en modo lectura y escritura

    with open('./Primer_Parcial_SuperMercado/sucursales.csv', mode='r', encoding='utf-8') as file:
        lector = csv.reader(file, delimiter=',')

        #next(reader)# Skip the header row
        for row in lector:
            tipoS = row[0]
            identif = row[1]
            superficie = row[2]
            totalfacturado = row[3]
            atributo5 = row[4]

            #nuevaSucursal = Sucursal(tipoS, identif, superficie, totalfacturado )
            if tipoS == '1':
                nuevaSucursal = Hiper(tipoS, identif, superficie, totalfacturado,  atributo5)
            elif tipoS == '2':
                nuevaSucursal = Supermercado(tipoS, identif, superficie, totalfacturado, atributo5 )
            else: #tipoS == '3'
                nuevaSucursal = Mini(tipoS, identif, superficie, totalfacturado, atributo5)
            
            print(f"Tipo: {tipoS}, ID: {identif}, Superficie: {superficie}, Total: {totalfacturado}, atributo 5: {row[4]}")
            #el atributo ser Mayorista 1 o NO (0) en el caso de Super,  
            # Alquiler Ganado en el caso de Hiper, 
            # o Alquiler Pagado en el caso de Mini
            
            print("agregar a la lista")
            listaSucursales.append(nuevaSucursal)
            print("agregado")
            print(f"Iteración número: {lector.line_num}")


def sumaGanancia():
    totalGanancia = 0
    for sucursal in listaSucursales:
        totalGanancia += sucursal.calcularGanancia()
    
    print(f"La ganancia total de todas las sucursales es de: {totalGanancia}$")

def localesNoRentables():
    totalNORentables = 0
    for sucursal in listaSucursales:
        if sucursal.esRentable() == False:
            totalNORentables += 1
            print(f"La sucursal de tipo: {sucursal.tipoS} nro id: {sucursal.identif} NO es rentable")
    print(f"La cantidad de locales NO rentables es de: {totalNORentables}")
            

def localMasRentable():
    IndiceRentabilidad = 0
    tipoLocal = None
    for sucursal in listaSucursales:
        if sucursal.calcularIndiceRentabilidad() > IndiceRentabilidad:
            IndiceRentabilidad = sucursal.calcularIndiceRentabilidad()
            tipoLocal = sucursal.tipoS
            idLocal = sucursal.identif
 
    print(f"La sucursal más rentable es de tipo: {tipoLocal} con ID: {idLocal} y rentabilidad: {IndiceRentabilidad}")
    
    #print(f"La sucursal mas rentable es: {localMasRentable.tipoS} nro id: {localMasRentable.identif} rentabilidad: {IndiceRentabilidad}")
    #print(f"La sucursal Mas retable : {localMasRentable} nro id: {localMasRentable.tipoS}, rentabilidad: {IndiceRentabilidad}")
    


if __name__ == "__main__":
    main()



