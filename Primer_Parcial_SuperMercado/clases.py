class Sucursal:
    def __init__(self, tipoS, identif, superficie, facturacion):
        self.tipoS = tipoS 
        self.identif = identif
        self.superficie = superficie
        self.facturacion = facturacion
        

    def __str__(self):
        return f"Tipo Sucursal: {self.tipoS}, Superficie: {self.superficie} m2, total: {self.facturacion}$"
    
    def __repr__(self):
        return f"Tipo Sucursal: {self.tipoS}, Superficie: {self.superficie} m2, total: {self.facturacion}$"
    
    def calcularIndiceRentabilidad(self):
        return (int(self.facturacion) / int(self.superficie))
    
    #def calcularGanancia(self):
        
    
    
    


"""Adicionalmente de cada sucursal existen dos cálculos sumamente relevantes:
 el resultado comercial y el índice de rentabilidad. 

 RESULTADO COMERCIAL:
tipo supermercado es resultadoC = facturación)
tipo hiper  resultadoC = facturacion + alquiler)
tipo Mini (resultadoC = facturacion - alquiler ) 

INDICE RENTABILIDAD:
Por otro lado, el índice de rentabilidad -> indiceR = (resultadoC/superficie)


hipermercado es rentable si                 índiceR > 50 
mini se considera rentable si su            índiceR > 35.
Los Super tradicionales son rentables si   índiceR >  40
Los Super mayoristas deben tener un        índiceR >  45. 

Se necesita un programa que lea del archivo sucursales.csv la lista de todas las sucursales y 
los almacene en algún objeto (no en la función
principal) que ofrezca los siguientes métodos:

1) Suma de ganancia: que informe el total del resultado comercial de todas las sucursales.

2) Cantidad de locales no rentables: que informe la cantidad de sucursales cuyo índice
 de rentabilidad sea menor al exigido.

3) Local más rentable: que informe número y tipo de la sucursal cuyo 
índice de rentabilidad sea el mayor de todos. 

La función principal debe ingresar los datos desde el archivo de texto y finalizar luego de imprimir el resultado de la ejecución de los tres métodos
anteriores. 

El archivo posee la siguiente estructura: 
1. Tipo de sucursal: 1 para hiper, 2 para super y 3 para mini
2. Número: número sin repetición que identifica cada sucursal
3. Superficie: número de tipo entero con la superficie en metros cuadrados
4. Facturación: número de tipo float con la facturación del local, expresada en miles de pesos
5. Si es  supermercado, un 1 si es mayorista y 0 si no lo es;
    Si es hipermercado, el importe ganado por alquileres;
   Si es  Mini, el importe pagado por el alquiler"""


class Supermercado(Sucursal):
    def __init__(self, tipoS, identif, superficie, facturacion, mayoristaONo):
        super().__init__(tipoS,identif, superficie, facturacion)
        self.mayoristaONO = mayoristaONo # 0 o 1
         
    def __str__(self):
        return f"Tipo Sucursal: {self.tipoS}, Superficie: {self.superficie} m2, total: {self.facturacion}$"
    
    def calcularIndiceRentabilidad(self):
        return super().calcularIndiceRentabilidad()
    
    def esRentable(self):
        #si es 1 Mayorista, 0 es TRADICIONAL
        if int(self.mayoristaONO) == 1 and self.calcularIndiceRentabilidad() > 45:
            return True
        elif int(self.mayoristaONO) == 0 and self.calcularIndiceRentabilidad() > 40:
            return True
        else:
            return False
        

    def esMayorista(self):
        if self.tipoS == 1:
            return True
        else:
            return False
            
    def calcularGanancia(self):
        return int(self.facturacion)
    

    
    
#***************************************** HIPER tipo 1 **************************************

class Hiper(Sucursal):
    def __init__(self, tipoS, identif, superficie, facturacion, importeA):
        super().__init__(tipoS,identif, superficie, facturacion)
        self.importeA = importeA
        
    
    
    def __str__(self):
        return f"Tipo Sucursal: {self.tipoS}, Superficie: {self.superficie} m2, total: {self.totalfacturado}$"
    
    def calcularIndiceRentabilidad(self):
        return super().calcularIndiceRentabilidad()
    
    def esRentable(self):
        if self.calcularIndiceRentabilidad() > 50:
            return True
        else:
            return False
        
    def calcularGanancia(self):
        return int(self.facturacion) - int(self.importeA)
 
    
#************************************************* MINI Tipo  3 ************************************
class Mini(Sucursal):
    def __init__(self, tipoS, identif, superficie, facturacion, importePagado):
        super().__init__(tipoS,identif, superficie, facturacion)
        self.importePagado = importePagado

    def __str__(self):
        return f"Tipo Sucursal: {self.tipoS}, Superficie: {self.superficie} m2,  total: {self.facturacion}$"
    
    def calcularIndiceRentabilidad(self):
        return super().calcularIndiceRentabilidad()
    
    
    
    def esRentable(self):
        if super().calcularIndiceRentabilidad() > 35:
            return True
        else:
            return False
    
    def calcularGanancia(self):
        return int(self.facturacion) - int(self.importePagado)

 
    