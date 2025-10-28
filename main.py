# Programa que utiliza listas, diccionarios y condicionales

from funciones import buscar_edad
from validaciones import validar_nombre
nombres = ["Yohel", "Demetrio", "Jonathan", "John", "Leonardo"]

edades = {
    "yohel": 29,
    "demetrio": 25,
    "jonathan": 27,
    "john": 25,
    "leonardo": 30
}

nombre = input("Ingresa un nombre: ").strip().lower()
nombre = validar_nombre(nombre)
# 👇 Se mantiene el if original
if nombre in edades:
    print(f"{nombre.capitalize()} tiene {edades[nombre]} años.")
    # 👇 Además, llamamos a tu función como refuerzo
    print(buscar_edad(nombre, edades))
else:
    print(f"{nombre.capitalize()} no fue encontrado en la lista.")
    # 👇 También usamos tu función en el else
    print(buscar_edad(nombre, edades))

