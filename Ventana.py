import tkinter as tk
from tkinter import ttk, messagebox

from generador import generar_contrasena
from archivos import guardar_password, leer_password


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración básica de la ventana
        self.title("Generador de Contraseñas")
        self.geometry("520x360")
        self.resizable(False, False)

        # Guardamos aquí la contraseña generada “actual”
        self.password_actual = ""

        # Variables de Tkinter: ayudan a leer/escribir lo que pone en las casillas
        self.var_longitud = tk.StringVar(value="12")
        self.var_mayus = tk.StringVar(value="2")
        self.var_especiales = tk.StringVar(value="2")
        self.var_digitos = tk.StringVar(value="2")
        self.var_archivo = tk.StringVar(value="password.txt")
        self.var_resultado = tk.StringVar(value="")

        self.crear_widgets()

    def crear_widgets(self):
        # Frame = “caja” para ordenar cosas dentro de la ventana
        main = ttk.Frame(self, padding=14)
        main.pack(fill="both", expand=True)

        ttk.Label(main, text="Generador de Contraseñas", font=("Arial", 16, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(0, 12)
        )

        # Entradas
        self.fila(main, "Longitud total:", self.var_longitud, 1)
        self.fila(main, "Nº mayúsculas:", self.var_mayus, 2)
        self.fila(main, "Nº especiales:", self.var_especiales, 3)
        self.fila(main, "Nº dígitos:", self.var_digitos, 4)
        self.fila(main, "Nombre del archivo:", self.var_archivo, 5)

        # Resultado (readonly para que se vea pero no se edite)
        ttk.Label(main, text="Contraseña generada:").grid(row=6, column=0, sticky="w", pady=(12, 4))
        ttk.Entry(main, textvariable=self.var_resultado, state="readonly", width=40).grid(
            row=7, column=0, columnspan=2, sticky="we"
        )

        # Botones
        botones = ttk.Frame(main)
        botones.grid(row=8, column=0, columnspan=2, pady=14)

        ttk.Button(botones, text="Generar", command=self.generar).grid(row=0, column=0, padx=6)
        ttk.Button(botones, text="Guardar", command=self.guardar).grid(row=0, column=1, padx=6)
        ttk.Button(botones, text="Recuperar", command=self.recuperar).grid(row=0, column=2, padx=6)
        ttk.Button(botones, text="Borrar", command=self.borrar).grid(row=0, column=3, padx=6)

        main.columnconfigure(1, weight=1)

    def fila(self, parent, texto, variable, row):
        # Crea una fila: etiqueta + cajita de escribir
        ttk.Label(parent, text=texto).grid(row=row, column=0, sticky="w", pady=4)
        ttk.Entry(parent, textvariable=variable, width=24).grid(row=row, column=1, sticky="w", pady=4)

    def generar(self):
        # 1) Convertimos las entradas a números
        try:
            L = int(self.var_longitud.get())
            M = int(self.var_mayus.get())
            E = int(self.var_especiales.get())
            D = int(self.var_digitos.get())
        except ValueError:
            messagebox.showerror("Error", "Longitud, mayúsculas, especiales y dígitos deben ser números enteros.")
            return

        # 2) Validaciones básicas (robustez)
        if L <= 0:
            messagebox.showerror("Error", "La longitud debe ser mayor que 0.")
            return
        if min(M, E, D) < 0:
            messagebox.showerror("Error", "No se permiten valores negativos.")
            return
        if M + E + D > L:
            messagebox.showerror("Error", "La suma (mayús + especiales + dígitos) no puede superar la longitud.")
            return

        # 3) Llamamos a la función del generador
        self.password_actual = generar_contrasena(L, M, E, D)

        # 4) Mostramos el resultado en la interfaz
        self.var_resultado.set(self.password_actual)

    def guardar(self):
        nombre = self.var_archivo.get().strip()

        if not self.password_actual:
            messagebox.showwarning("Aviso", "Primero genera una contraseña antes de guardar.")
            return
        if not nombre:
            messagebox.showerror("Error", "Escribe un nombre de archivo válido.")
            return

        try:
            guardar_password(nombre, self.password_actual)
            messagebox.showinfo("OK", f"Guardado en '{nombre}'.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar.\n\nDetalle: {e}")

    def recuperar(self):
        nombre = self.var_archivo.get().strip()

        if not nombre:
            messagebox.showerror("Error", "Escribe un nombre de archivo válido.")
            return

        try:
            contenido = leer_password(nombre)
            self.password_actual = contenido
            self.var_resultado.set(contenido)
            messagebox.showinfo("OK", f"Recuperado desde '{nombre}'.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Ese archivo no existe.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer.\n\nDetalle: {e}")

    def borrar(self):
        # Deja todo “como al principio”
        self.var_longitud.set("12")
        self.var_mayus.set("2")
        self.var_especiales.set("2")
        self.var_digitos.set("2")
        self.var_archivo.set("password.txt")
        self.var_resultado.set("")
        self.password_actual = ""


if __name__ == "__main__":
    app = App()
    app.mainloop()



