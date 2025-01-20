class Maquina():

    def __init__(self):
        self.mantenimientos = []
        self.cargar_datos()

    def __str__(self):
        texto = "**************** \n"
        for m in self.mantenimientos:
            texto += str(m)+"\n"
        texto += " FIN "
        return texto

    def cargar_datos(self):
        #paso 1 abrir el archivo
        file = open("./Primer_Parcial_Fabrica/mantenimientos.csv", 'rt')
        #paso 2 - Recorrerlo y obtener sus campos
        for linea in file:
            campos = linea[:-1].split(',')
            tipo =  int(campos[0])
            fecha = campos[1]
            operario = campos[2]
            importe = float(campos[3])
            
            #Paso 3 - Preguntar de que tipo son y crear el Mantenimiento según el tipo
            #Paso 4 - Agregarlos a la lista.
            if (tipo == 1):
                resultado = int(campos[4])
                importeInsumos = float(campos[5])
                mantenimiento = Preventivo(tipo, fecha, operario, importe, resultado, importeInsumos)

            else:
                horas = campos[4]
                importeTecnico = float(campos[5])
                mantenimiento = Correctivo(tipo, fecha, operario, importe, horas, importeTecnico)
            
            self.mantenimientos.append(mantenimiento)
        file.close()

    def suma_Gastos(self):
        suma = 0 
        for m in self.mantenimientos: 
            suma += m.get_Costo()
        return suma

    def cant_Mant_Caros(self):
        #los mantenimientos que superen los $10.000
        mantenimientos_Caros = [m for m in self.mantenimientos if (m.get_Costo() > 10000) ]
        return len(mantenimientos_Caros)

    #que informe la fecha y el nombre del operario del mantenimiento correctivo de mayor duración.
    def rotura_Mas_Larga(self):
        mant = Correctivo(2,None,None,0,0,0)
         
        for m in self.mantenimientos: 
            if (m.tipo == 2 and int(m.horasParada) > int(mant.horasParada)):
                mant = m
        return mant

class Mantenimiento():
    #Tiene los atributos de la superclase.
    def __init__(self, tipo, fecha, operario,importe):
        self.tipo =  tipo
        self.fecha =  fecha
        self.operario =  operario
        self.importe = importe

    def __str__(self):
        return f"El mantenimiento hecho por el operario {self.operario}  con importe: {self.importe}"
    
class Preventivo(Mantenimiento):
    def __init__(self,tipo, fecha, operario, importe, resultado, importeInsumo ):
        super().__init__(tipo,fecha,operario, importe)
        self.resultado = resultado
        self.importeInsumo = importeInsumo

    def __str__(self):
        mantenimiento_str_ = super().__str__()
        texto = f"PREVENTIVO {mantenimiento_str_}, resultado {self.resultado}, importe: {self.importeInsumo}"
        return texto

    def get_Costo(self):
        return (self.importe + self.importeInsumo)


class Correctivo(Mantenimiento):
    def __init__(self, tipo, fecha, operario, importe, horasParada, importeTecnico):
        super().__init__(tipo, fecha, operario, importe)    
        self.horasParada = horasParada
        self.importeTecnico = importeTecnico

    def __str__(self):
        m = super().__str__()
        texto = f"CORRECTIVO {m}, horas parada: {self.horasParada}, importe técnico: {self.importeTecnico}"
        return texto

    def get_Costo(self):
        return (self.importe + self.importeTecnico)