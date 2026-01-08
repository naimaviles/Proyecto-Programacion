import tkinter as tk
from tkinter import messagebox

# Importamos las funciones del proyecto
from generador import generar_contrasena
from archivos import guardar_password, leer_password


def main():
    # -------------------------
    # Ventana principal
    # -------------------------
    ventana = tk.Tk()
    ventana.title("Generador de Contraseñas")
    ventana.geometry("520x380")
    ventana.resizable(False, False)

    BG_COLOR = "#E9A9F9"
    ventana.configure(bg=BG_COLOR)

    password_actual = ""  # Aquí guardamos la última contraseña generada

    # Variable donde mostraremos la contraseña generada
    resultado_var = tk.StringVar(value="")

    # -------------------------
    # Funciones de los botones
    # -------------------------
    def generar():
        """Lee los datos, valida y genera la contraseña."""
        nonlocal password_actual

        try:
            L = int(entrada_longitud.get())
            M = int(entrada_mayus.get())
            E = int(entrada_especiales.get())
            D = int(entrada_digitos.get())
        except ValueError:
            messagebox.showerror("Error", "Introduce números enteros válidos.")
            return

        # Validaciones básicas (robustez)
        if L <= 0:
            messagebox.showerror("Error", "La longitud debe ser mayor que 0.")
            return
        if min(M, E, D) < 0:
            messagebox.showerror("Error", "No se permiten valores negativos.")
            return
        if M + E + D > L:
            messagebox.showerror("Error", "La suma (mayús + especiales + dígitos) no puede superar la longitud.")
            return

        # Generar contraseña
        password_actual = generar_contrasena(L, M, E, D)

        # Mostrarla en la interfaz
        resultado_var.set(password_actual)

    def guardar():
        """Guarda la contraseña actual en un archivo."""
        nombre = entrada_archivo.get().strip()

        if password_actual == "":
            messagebox.showwarning("Aviso", "Primero genera una contraseña.")
            return
        if nombre == "":
            messagebox.showerror("Error", "Escribe un nombre de archivo válido (ej: password.txt).")
            return

        try:
            guardar_password(nombre, password_actual)
            messagebox.showinfo("OK", f"Contraseña guardada en '{nombre}'.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar.\n\nDetalle: {e}")

    def recuperar():
        """Lee la contraseña desde un archivo y la muestra."""
        nonlocal password_actual
        nombre = entrada_archivo.get().strip()

        if nombre == "":
            messagebox.showerror("Error", "Escribe un nombre de archivo válido.")
            return

        try:
            contenido = leer_password(nombre)
            if contenido == "":
                messagebox.showwarning("Aviso", f"El archivo '{nombre}' está vacío.")
                return

            password_actual = contenido
            resultado_var.set(contenido)
            messagebox.showinfo("OK", f"Contraseña recuperada desde '{nombre}'.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Ese archivo no existe.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer.\n\nDetalle: {e}")

    def borrar():
        """Deja todo como al principio."""
        nonlocal password_actual

        entrada_longitud.delete(0, tk.END)
        entrada_longitud.insert(0, "12")

        entrada_mayus.delete(0, tk.END)
        entrada_mayus.insert(0, "2")

        entrada_especiales.delete(0, tk.END)
        entrada_especiales.insert(0, "2")

        entrada_digitos.delete(0, tk.END)
        entrada_digitos.insert(0, "2")

        entrada_archivo.delete(0, tk.END)
        entrada_archivo.insert(0, "password.txt")

        password_actual = ""
        resultado_var.set("")

    # -------------------------
    # Widgets (como en clase)
    # -------------------------
    titulo = tk.Label(
        ventana,
        text="Generador de Contraseñas",
        font=("Arial", 16, "bold"),
        bg=BG_COLOR
    )
    titulo.pack(pady=(14, 10))

    # Longitud
    tk.Label(ventana, text="Longitud total:", bg=BG_COLOR).pack()
    entrada_longitud = tk.Entry(ventana)
    entrada_longitud.pack()
    entrada_longitud.insert(0, "12")

    # Mayúsculas
    tk.Label(ventana, text="Nº mayúsculas:", bg=BG_COLOR).pack()
    entrada_mayus = tk.Entry(ventana)
    entrada_mayus.pack()
    entrada_mayus.insert(0, "2")

    # Especiales
    tk.Label(ventana, text="Nº especiales:", bg=BG_COLOR).pack()
    entrada_especiales = tk.Entry(ventana)
    entrada_especiales.pack()
    entrada_especiales.insert(0, "2")

    # Dígitos
    tk.Label(ventana, text="Nº dígitos:", bg=BG_COLOR).pack()
    entrada_digitos = tk.Entry(ventana)
    entrada_digitos.pack()
    entrada_digitos.insert(0, "2")

    # Archivo
    tk.Label(ventana, text="Nombre del archivo (ej: password.txt):", bg=BG_COLOR).pack(pady=(8, 0))
    entrada_archivo = tk.Entry(ventana)
    entrada_archivo.pack()
    entrada_archivo.insert(0, "password.txt")

    # Resultado
    tk.Label(ventana, text="Contraseña generada:", bg=BG_COLOR).pack(pady=(12, 0))
    entrada_resultado = tk.Entry(ventana, textvariable=resultado_var, state="readonly", width=45)
    entrada_resultado.pack()

    # Botones
    frame_botones = tk.Frame(ventana, bg=BG_COLOR)
    frame_botones.pack(pady=14)

    tk.Button(frame_botones, text="Generar", command=generar, width=10).grid(row=0, column=0, padx=6)
    tk.Button(frame_botones, text="Guardar", command=guardar, width=10).grid(row=0, column=1, padx=6)
    tk.Button(frame_botones, text="Recuperar", command=recuperar, width=10).grid(row=0, column=2, padx=6)
    tk.Button(frame_botones, text="Borrar", command=borrar, width=10).grid(row=0, column=3, padx=6)

    # Mantener la ventana abierta
    ventana.mainloop()


if __name__ == "__main__":
    main()
