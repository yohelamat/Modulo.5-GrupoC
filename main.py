# Programa que utiliza listas, diccionarios y condicionales

from funciones import buscar_edad
from validaciones import validar_nombre

# Lista con nombres
nombres = ["Yohel", "Demetrio", "Jonathan", "John", "Leonardo"]

# Diccionario con edades
edades = {
    "yohel": 29,
    "demetrio": 25,
    "jonathan": 27,
    "john": 25,
    "leonardo": 30
}

# Solicitar nombre al usuario
nombre = input("Ingresa un nombre: ").strip().lower()
nombre = validar_nombre(nombre)

# Muestra el resultado
resultado = buscar_edad(nombre, edades)
print(resultado)
