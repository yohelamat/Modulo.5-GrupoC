# Programa que utiliza listas, diccionarios y condicionales

from funciones import buscar_edad

nombres = ["Yohel", "Demetrio", "Jonathan", "John", "Leonardo"]

edades = {
    "yohel": 29,
    "demetrio": 25,
    "jonathan": 27,
    "john": 25,
    "leonardo": 30
}

nombre = input("Ingresa un nombre: ").strip().lower()

resultado = buscar_edad(nombres, edades)

print(resultado)