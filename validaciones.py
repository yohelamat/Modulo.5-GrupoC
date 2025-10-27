# =========================================================
# validaciones.py
# Rol: Validar entradas - John Roa
# =========================================================

def validar_nombre(nombre):
    """
    Valida y limpia el nombre ingresado por el usuario.
    - Elimina espacios en blanco.
    - Convierte la primera letra a mayúscula.
    - Retorna None si la entrada está vacía o contiene solo espacios.
    """

    # Eliminar espacios al inicio y al final
    nombre = nombre.strip()

    # Verificar si el nombre está vacío
    if not nombre:
        return None

    # Formatear: primera letra mayúscula, resto minúsculas
    nombre = nombre.capitalize()

    return nombre
