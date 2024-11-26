class Maquina:
    def cargar_datos(self):
        file = open('.\mantenimientos.csv','rt')
        for linea in file:
            campos = linea[:-1].split(',')
            tipo = int(campos[0])
            fecha = campos[1]
            operario=campos[2]
            importe=campos[3]

    def cargar(self):
        file = open(".\ruta.csv",'rt')
        for linea in file:
            campos = linea[:-1].split(',')
            tipo = campos[0]

            if (tipo == 1):
                #creo un preventivo
                #mantenimiento = Preventivo( valores)
            else:
                #creo un tipo correctivo 
                #mantenimiento = Correctivo(valor1, 2,3,4)
            

            #self.mantenimientos.append(mantenimiento)
        file.close()




''' Tipo de mantenimiento: 1 para preventivo y 2 para correctivo
2. Fecha: una cadena
3. Operario: nombre del operario que realizó el mantenimiento
4. Importe de repuestos: número de tipo float
5. Si es un preventivo, resultado del mantenimiento (1, 2 o 3); si es un correctivo, cantidad de horas de parada.
6. Si es un preventivo, importe de los insumos; si es un correctivo, importe que cobró el técnic'''