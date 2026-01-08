# Guardar y leer la contraseña en un archivo de texto.
def guardar_password(nombre_archivo, password):
    # "w" = escribir (sobrescribe el archivo)
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(password)

def leer_password(nombre_archivo):
    # "r" = leer
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        return f.read().strip()
