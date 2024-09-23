class Mantenimiento:
    def __init__(self, tipoM, fecha, operario, importe):
        self.tipoM = tipoM  # 1 or 2
        self.fecha = fecha  # string
        self.operario = operario  # string
        self.importe = importe  # float


    def mostrar(self):
        print(f"Tipo de mantenimiento: {self.tipoM}")
        print(f"Fecha: {self.fecha}")
        print(f"Operario: {self.operario}")
        print(f"Importe: {self.importe}")
        print(f"Horas: {self.horas}")

    def __str__(self):
        return f"{self.tipoM}, {self.fecha}, {self.operario}, {self.importe}"
    


class Preventivo(Mantenimiento):
    def __init__(self, tipoM, fecha, operario, importe,  resultado, importeTecnico):
        super().__init__(tipoM, fecha, operario, importe)
        
        self.resultado = resultado  # 1, 2, or 3
        self.importeTecnico = importeTecnico  # float
        

    def mostrar(self):
        super().mostrar()
        print(f"Resultado: {self.resultado}")

    def __str__(self):
        return f"{super().self},{self.resultado},{self.importeTecnico}"
    


class Correctivo(Mantenimiento):
    def __init__(self, tipoM, fecha, operario, importe, horas, importeTecnico):
        super().__init__(tipoM, fecha, operario, importe)
        
        self.horas = horas  #int
        self.importeTecnico = importeTecnico  #int
    
    def mostrar(self):
        super().mostrar()
        print(f"Horas: {self.horas}")

    def __str__(self):
        return f"{super().self},{self.horas},{self.importeTecnico}" 

class Maquina:
    def __init__(self, id, nombre):
        self.id = id  # int
        self.nombre = nombre  # string
        self.mantenimientos = []  # list of Mantenimiento objects


    def agregar_mantenimiento(self, mantenimiento):
        if isinstance(mantenimiento, Mantenimiento):
            self.mantenimientos.append(mantenimiento)
        else:
            raise TypeError("El mantenimiento debe ser una instancia de la clase Mantenimiento")
        
    def mostrar_mantenimientos(self):
        for mantenimiento in self.mantenimientos:
            mantenimiento.mostrar()
            print()




