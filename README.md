## Funcionalidades

1. **Generar Contraseña**
   - Campos:
     - Longitud total
     - Nº de mayúsculas
     - Nº de caracteres especiales
     - Nº de dígitos
   - Cumple exactamente con las cantidades indicadas y **rellena el resto con minúsculas**.
   - El resultado se **baraja** para evitar patrones o bloques de caracteres.

2. **Guardar Contraseña en Fichero**
   - Solicita el nombre del archivo, por ejemplo: `password.txt`
   - Si no hay contraseña generada, se muestra el mensaje:
     > _"Primero genera una contraseña."_
   - Si el nombre del archivo está vacío:
     > _"Escribe un nombre de archivo válido (ej: password.txt)."_

3. **Recuperar Contraseña de Fichero**
   - Solicita el nombre del archivo.
   - Si el archivo no existe:
     > _"Ese archivo no existe."_
   - Si el archivo está vacío:
     > _"El archivo '<nombre>' está vacío."_
   - La contraseña recuperada se muestra en la interfaz.

4. **Borrar campos**
   - Restablece los valores por defecto:
     - Longitud = `12`
     - Mayúsculas = `2`
     - Especiales = `2`
     - Dígitos = `2`
     - Archivo = `password.txt`
   - Limpia el resultado mostrado y el estado interno del programa.

---

## Validación de datos

Antes de generar la contraseña, el programa valida los datos introducidos por el usuario mediante la función `validar_datos`, ubicada en el archivo `validaciones.py`.

Se comprueba que:
- Ningún campo esté vacío.
- Todos los valores sean números enteros positivos.
- La longitud total sea mayor que cero.
- La suma de mayúsculas, caracteres especiales y dígitos no supere la longitud total de la contraseña.

Si alguna de estas condiciones no se cumple, la generación de la contraseña se bloquea y se muestra
un mensaje de error al usuario.

---

## Requisitos

- **Python 3.10 o superior** (recomendado)
- **Tkinter** (incluido por defecto en la mayoría de instalaciones de Python)
- Uso exclusivo de **bibliotecas estándar**:
  - `tkinter`
  - `string`
  - `random`
  - `os` (opcional)

---

## Cómo ejecutar

### Desde la interfaz gráfica

Ejecutar el siguiente comando desde la carpeta del proyecto:

```bash
python ventana.py
