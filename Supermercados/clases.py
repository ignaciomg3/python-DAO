class Empresa:
    def cargar_datos(self):
        file = open("./sucursales.csv",'rt')  
        for linea in file:
            campos = linea[:-1].split(',')
            tipo = int(campos[0])
            numero = int(campos[1])
            sup = int(campos[2])
            fac = float(campos[3])

            #preguntamos los datos q son distintos en los supermercados

            #tipo HIPER
            if (tipo == 1):
                ganado = float(campos[4])
                sucursal = Hiper(tipo, numero, sup, fac, ganado)
            #tipo SUPER
            if(tipo == 2):
                tipoSuper = int(campos[4])
                sucursal = Super(tipo,numero, sup,fac, tipoSuper)
            else:
                pagado = float(campos[4])
                sucursal = Mini(tipo,numero, sup,fac,pagado)
            
            self.sucursales.append(sucursal)
        file.close()

    def __str__(self):
        txt = "--- Informe ---\n"
        for suc in self.sucursales:
            txt += str(suc)+"\n"
        txt += "--- ### ---"
        return txt
    
    def __init__(self):
        self.sucursales = []
        #rellenamos la lista de sucursales
        self.cargar_datos()
        self.positivas = 0
        self.negativas = 0

    def get_PositivasYNegativas(self):
        for s in self.sucursales:
            if(s.get_Ganancia() > 0):
                self.positivas += s.get_Ganancia()
            else:
                self.negativas += s.get_Ganancia()

    def mostrar_todas_las_ganancias(self):
        for s in self.sucursales:
            s.get_Ganancia() 

    #Punto 1
    def sumar_Ganancias(self):
        ganancias_Totales = 0
        for s in self.sucursales : 
            ganancias_Totales += s.get_Ganancia()
        return ganancias_Totales
    
    def mostrar_Ganancias(self):
        for s in self.sucursales:
            print(s.get_Ganancia())
           
    #Punto 2
    def cantidad_NO_Rentables(self):
        '''Cantidad de locales no rentables: que informe la cantidad de sucursales cuyo índice de rentabilidad sea menor al exigido.'''
        cantidad_NO_Rentables = 0
        for s in self.sucursales:
            if not s.es_Rentable():
                cantidad_NO_Rentables +=1
        return  cantidad_NO_Rentables
    #Punto 3
    def mas_rentable(self):
        '''Local más rentable: que informe número y tipo de la sucursal cuyo índice de rentabilidad sea el mayor de todos.'''
        iRentabilidad = 0
        sucursalMasRentable = None
        print("hola")
        for s in self.sucursales:
            if(s.get_IndiceRentabilidad() > iRentabilidad):
                print(f"La el indice nuevo: {s.get_IndiceRentabilidad()} y el viejo es: {iRentabilidad}")
                print(f"numero de sucursal {s.numero}")
                sucursalMasRentable = s
                iRentabilidad = s.get_IndiceRentabilidad()
        return print(f"La sucursal mas rentable es la número {sucursalMasRentable.numero}, tipo: {sucursalMasRentable.tipo} y su índice es: {sucursalMasRentable.get_IndiceRentabilidad()}")
    

class Sucursal:
    def __init__(self,tipo,numero, sup, fac):
        self.tipo =tipo
        self.numero = numero
        self.sup=sup
        self.fac=fac

    def __str__(self):
        return f"TIPO: {self.tipo}, numero: {self.numero} SUPERFICIE: {self.sup}, FACTURACION: {self.fac}"
    
class Hiper(Sucursal):
    def __init__(self,tipo,numero, sup,fac, ganancia):
        super().__init__(tipo,numero,sup,fac)
        self.ganancia = ganancia

    def __srt__(self):
        suc_srt = super().__srt__()
        srt = f"HIPERMERCADO >> {suc_srt} GANANCIA {self.ganancia}"
        return srt
    
    def get_ResultadoComercial(self):
        return (self.fac + self.ganancia)
    
    def get_IndiceRentabilidad(self):
        indice = round(float(self.get_ResultadoComercial() / self.sup), 2)
        return indice

    def es_Rentable(self):
        return (self.get_IndiceRentabilidad > 50)
    
    def get_Ganancia(self):
        return (self.fac + self.ganancia)
    
class Super(Sucursal):
    def __init__(self, tipo,numero,sup,fac,tipoSuper):
        super().__init__(tipo,numero,sup,fac)
        self.tipoSuper  = tipoSuper

           
    def __str__(self):
        suc_str = super().__str__()
        tradicional_Mayorista = self.tradOMay() 
        str = f"SUPERMERCADO {suc_str} Tipo {tradicional_Mayorista}"
        return str

    def get_IndiceRentabilidad(self):
        return round(float(self.fac / self.sup),2)
    
    def es_Rentable(self):
        if(self.tradOMay() == "Mayorista"): 
            return self.get_IndiceRentabilidad() > 45
        else:
            return self.get_IndiceRentabilidad() > 40
        
    def get_Ganancia(self):
        return self.fac
    
    def tradOMay(self):
        if (self.tipoSuper == 1):
            return "Mayorista"
        else:
            return "Tradicional"
    

class Mini(Sucursal):
    def __init__(self,tipo,numero,sup,fac, pagado):
        super().__init__(tipo,numero, sup,fac)
        self.pagado = pagado

    def __str__(self):
        super_str = super().__str__()
        str = f"SUCURSAL >> {super_str}, Pagado: {self.pagado}"
        return str
    
    def get_ResultadoComercial(self):
        resultadoComercial = float(self.fac - self.pagado)
        return resultadoComercial
    
    def get_IndiceRentabilidad(self):
        return round(float(self.get_ResultadoComercial() / self.sup),2)
    
    def es_Rentable(self):
        return self.get_IndiceRentabilidad() > 35
    
    def get_Ganancia(self):
        return (self.fac - self.pagado)




        
