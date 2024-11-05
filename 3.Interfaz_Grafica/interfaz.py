import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importar ttk para un estilo mejorado
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Función que se ejecuta al hacer clic en "Enviar"
def enviar_datos():
    nombre = entry_nombre.get()
    correo = entry_correo.get()

    # Validar que los campos no estén vacíos
    if not nombre or not correo:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
    else:
        # Aquí puedes manejar los datos enviados
        messagebox.showinfo("Datos Enviados", f"Nombre: {nombre}\nCorreo: {correo}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario con Estilo Moderno")
ventana.geometry("300x200")
# Establecer la resolución mínima (ancho x alto)
ventana.minsize(300, 300)  # Ancho mínimo de 300 píxeles y alto mínimo de 200 píxeles

#**************************** LOGO UTN ***************************
# Cargar la imagen usando Pillow
imagen = Image.open("3.Interfaz_Grafica/utn.png")

# Redimensionar la imagen a 150x150 píxeles, por ejemplo
imagen_redimensionada = imagen.resize((100, 100))

# Convertir la imagen redimensionada a un formato compatible con Tkinter
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

# Crear un Label con la imagen
logo = tk.Label(ventana, image=imagen_tk)

# Posicionar la imagen con el método pack (centrado con padding)
#logo.pack(padx=0, pady=0)  # Puedes ajustar el padding para controlar la posición

# Si quieres más control de la posición, usa place() con coordenadas exactas:
logo.place(x=0, y=0)  # Esto lo coloca en la posición (100, 100) de la ventana

#**************************** ***************************


# Etiqueta y campo de entrada para el nombre
label_nombre = ttk.Label(ventana, text="Nombre:")
label_nombre.pack(pady=5)

entry_nombre = ttk.Entry(ventana)
entry_nombre.pack(pady=5)

# Etiqueta y campo de entrada para el correo
label_correo = ttk.Label(ventana, text="Correo:")
label_correo.pack(pady=5)

entry_correo = ttk.Entry(ventana)
entry_correo.pack(pady=5)

# Botón para enviar los datos
boton_enviar = ttk.Button(ventana, text="Enviar", command=enviar_datos)
boton_enviar.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
