import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función que valida el usuario y la contraseña
def validar_login():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()
    
    if usuario == "admin" and contraseña == "12345":
        messagebox.showinfo("Login exitoso", "¡Bienvenido!")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("300x200")

# Crear un frame para organizar los widgets con ttk
frame = ttk.Frame(ventana, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

# Etiqueta para "Usuario"
ttk.Label(frame, text="Usuario:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Entrada para el usuario
entrada_usuario = ttk.Entry(frame, width=25)
entrada_usuario.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta para "Contraseña"
ttk.Label(frame, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

# Entrada para la contraseña (con ocultación de texto)
entrada_contraseña = ttk.Entry(frame, width=25, show="*")
entrada_contraseña.grid(row=1, column=1, padx=5, pady=5)

# Botón de login
boton_login = ttk.Button(frame, text="Login", command=validar_login)
boton_login.grid(row=2, column=0, columnspan=2, pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
