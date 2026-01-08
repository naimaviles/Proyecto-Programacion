## Funcionalidades

1. **Generar Contraseña**
   - Campos:
     - Longitud total
     - Nº de mayúsculas
     - Nº de caracteres especiales
     - Nº de dígitos
   - Cumple exactamente con las cantidades indicadas y **rellena el resto con minúsculas**. El resultado se **baraja** para no dejar bloques juntos.

2. **Guardar Contraseña en Fichero**
   - Pide nombre de archivo, por ejemplo: `password.txt`
   - Si no hay contraseña generada, avisa:
     > _"Primero genera una contraseña."_
   - Si el nombre de archivo está vacío, avisa:
     > _"Escribe un nombre de archivo válido (ej: password.txt)."_

3. **Recuperar Contraseña de Fichero**
   - Pide nombre de archivo
   - Si el archivo no existe:  
     > _"Ese archivo no existe."_
   - Si está vacío:  
     > _"El archivo '<nombre>' está vacío."_
   - Muestra la contraseña recuperada en la interfaz

4. **Borrar campos**
   - Restablece valores por defecto:
     - Longitud = `12`
     - Mayúsculas = `2`
     - Especiales = `2`
     - Dígitos = `2`
     - Archivo = `password.txt`
   - Limpia el resultado y el estado interno

## ✅ Validaciones implementadas

Desde `validaciones.py`:

- No se permiten **campos vacíos**
- Solo **enteros positivos**
- **Longitud > 0**
- **Coherencia**: `mayúsculas + especiales + dígitos ≤ longitud`

Si algo falla, la GUI muestra:  
> _"Datos no válidos. Revisa los campos."_


## Requisitos

- **Python 3.10+** (recomendado)
- **Tkinter** (incluido en instalaciones estándar de Python en la mayoría de sistemas)
- Solo usa **biblioteca estándar**:
  - `tkinter`, `string`, `random`, `os` (opcional)


## Cómo ejecutar
### Desde Interfaz gráfica 

```bash
python ventana.py

