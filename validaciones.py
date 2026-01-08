def validar_datos(longitud, mayusculas, especiales, digitos):
    # Limpiar espacios
    longitud = longitud.strip()
    mayusculas = mayusculas.strip()
    especiales = especiales.strip()
    digitos = digitos.strip()

    # 1. Campos vacíos
    if not longitud or not mayusculas or not especiales or not digitos:
        return False

    # 2. Deben ser números enteros positivos
    if not longitud.isdigit() or not mayusculas.isdigit() or not especiales.isdigit() or not digitos.isdigit():
        return False

    # 3. Convertir a int
    longitud = int(longitud)
    mayusculas = int(mayusculas)
    especiales = int(especiales)
    digitos = int(digitos)

    # 4. Valores válidos
    if longitud <= 0:
        return False

    # 5. Coherencia con el generador
    if mayusculas + especiales + digitos > longitud:
        return False

    return True
