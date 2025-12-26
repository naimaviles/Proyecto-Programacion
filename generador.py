import string
import random  

def generar_contrasena(longitud, n_mayus, n_especiales, n_digitos):

    if longitud <= 0:
        raise ValueError("La longitud debe ser mayor que 0")
    if n_mayus < 0 or n_especiales < 0 or n_digitos < 0:
        raise ValueError("Las cantidades no pueden ser negativas")

    minimo_requerido = n_mayus + n_especiales + n_digitos
    if minimo_requerido > longitud:
        raise ValueError(
            f"No cuadra: {minimo_requerido} > longitud({longitud})"
        )

    # Conjuntos de caracteres
    letras_mayus = string.ascii_uppercase
    letras_minus = string.ascii_lowercase
    digitos = string.digits
    especiales = "!@#$%^&*()-_=+[]{};:,.?/"

    chars = []

    # Añadir exactamente la cantidad deseada de mayúsculas
    for _ in range(n_mayus):
        chars.append(random.choice(letras_mayus))

    # Añadir exactamente la cantidad deseada de caracteres especiales
    for _ in range(n_especiales):
        chars.append(random.choice(especiales))

    # Añadir exactamente la cantidad deseada de dígitos
    for _ in range(n_digitos):
        chars.append(random.choice(digitos))

    # Rellenar con minúsculas
    restantes = longitud - len(chars)
    for _ in range(restantes):
        chars.append(random.choice(letras_minus))

    # Mezclar para que no queden los elementos de cada grupo agrupados
    random.shuffle(chars)

    return "".join(chars)

# Programa principal
if __name__ == "__main__":
    print("GENERADOR DE CONTRASEÑAS:")
    L = int(input("Longitud total deseada: "))
    M = int(input("Cantidad exacta de MAYÚSCULAS: "))
    E = int(input("Cantidad exacta de caracteres ESPECIALES: "))
    D = int(input("Cantidad exacta de DÍGITOS: "))

    try:
        password = generar_contrasena(L, M, E, D)
        print("\nContraseña generada:")
        print(password)
    except ValueError as err:
        print("\n[ERROR]", err)
