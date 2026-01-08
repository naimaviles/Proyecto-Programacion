import tkinter as tk
from tkinter import messagebox

from generador import generar_contrasena
from archivos import guardar_password, leer_password


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Generador de Contraseñas")
        self.geometry("520x360")
        self.resizable(False, False)

        # Fondo claro para que en macOS dark mode se vea todo
        self.configure(bg="white")

        self.password_actual = ""

        # Variables (lo que hay en las cajitas)
        self.var_longitud = tk.StringVar(value="12")
        self.var_mayus = tk.StringVar(value="2")
        self.var_especiales = tk.StringVar(value="2")
        self.var_digitos = tk.StringVar(value="2")
        self.var_archivo = tk.StringVar(value="password.txt")
        self.var_resultado = tk.StringVar(value="")

        self.crear_widgets()

    def crear_widgets(self):
        titulo = tk.Label(self, text="Generador de Contraseñas",
                          font=("Arial", 16, "bold"), bg="white")
        titulo.pack(pady=(14, 10))

        form = tk.Frame(self, bg="white")
        form.pack(padx=14, fill="x")

        self.fila(form, "Longitud total:", self.var_longitud)
        self.fila(form, "Nº mayúsculas:", self.var_mayus)
        self.fila(form, "Nº especiales:", self.var_especiales)
        self.fila(form, "Nº dígitos:", self.var_digitos)
        self.fila(form, "Nombre del archivo:", self.var_archivo)

        tk.Label(self, text="Contraseña generada:", bg="white").pack(pady=(12, 4))

        # readonly de verdad (pero visible)
        entry_res = tk.Entry(self, textvariable=self.var_resultado, width=45, state="readonly")
        entry_res.pack()

        botones = tk.Frame(self, bg="white")
        botones.pack(pady=14)

        tk.Button(botones, text="Generar", command=self.generar, width=10).grid(row=0, column=0, padx=6)
        tk.Button(botones, text="Guardar", command=self.guardar, width=10).grid(row=0, column=1, padx=6)
        tk.Button(botones, text="Recuperar", command=self.recuperar, width=10).grid(row=0, column=2, padx=6)
        tk.Button(botones, text="Borrar", command=self.borrar, width=10).grid(row=0, column=3, padx=6)

    def fila(self, parent, texto, variable):
        fila = tk.Frame(parent, bg="white")
        fila.pack(fill="x", pady=4)

        tk.Label(fila, text=texto, width=18, anchor="w", bg="white").pack(side="left")
        tk.Entry(fila, textvariable=variable, width=25).pack(side="left")

    def generar(self):
        try:
            L = int(self.var_longitud.get())
            M = int(self.var_mayus.get())
            E = int(self.var_especiales.get())
            D = int(self.var_digitos.get())
        except ValueError:
            messagebox.showerror("Error", "Los campos numéricos deben ser enteros.")
            return

        if L <= 0:
            messagebox.showerror("Error", "La longitud debe ser mayor que 0.")
            return
        if min(M, E, D) < 0:
            messagebox.showerror("Error", "No se permiten valores negativos.")
            return
        if M + E + D > L:
            messagebox.showerror("Error", "La suma (mayús + especiales + dígitos) no puede superar la longitud.")
            return

        self.password_actual = generar_contrasena(L, M, E, D)
        self.var_resultado.set(self.password_actual)

    def guardar(self):
        nombre = self.var_archivo.get().strip()

        if not self.password_actual:
            messagebox.showwarning("Aviso", "Primero genera una contraseña.")
            return
        if not nombre:
            messagebox.showerror("Error", "Escribe un nombre de archivo válido.")
            return

        guardar_password(nombre, self.password_actual)
        messagebox.showinfo("OK", f"Guardado en '{nombre}'.")

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

    def borrar(self):
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
