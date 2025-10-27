# funciones.py

def buscar_edad(nombre, diccionario):
    """
    Busca la edad de una persona en el diccionario.
    Retorna un mensaje personalizado si se encuentra o no.
    """
    nombre = nombre.strip().lower()
    if nombre in diccionario:
        return f"{nombre.capitalize()} tiene {diccionario[nombre]} años."
    else:
        return f"{nombre.capitalize()} no fue encontrado en la lista."
