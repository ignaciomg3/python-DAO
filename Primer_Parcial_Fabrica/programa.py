def main():
    while True:
        opcion = menuOpciones()
        if opcion == '1':
            print("Has elegido la opción 1: Suma de dos números")
            suma()
        elif opcion == '2':
            print("Has elegido la opción 2: Mostrar un mensaje")
            mostrarMensaje()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def menuOpciones():
    print("**************************** MENÚ DE OPCIONES ****************************")
    print("1. Suma de dos números")
    print("2. Mostrar un mensaje")
    print("3. Salir del programa")
    return input("Elige una opción: ")

def suma():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    print(f"La suma es: {num1 + num2}")

def mostrarMensaje():
    print("¡Hola! Este es un mensaje simple.")

if __name__ == "__main__":
    main()
