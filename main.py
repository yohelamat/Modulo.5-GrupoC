# Programa que utiliza listas, diccionarios y condicionales

from funciones import buscar_edad

nombres = ["Yohel", "Demetrio", "Jonathan", "John", "Leonardo"]
edades = [29, 25, 27, 25, 30]

edades = {
    nombre.lower(): edad for nombre, edad in zip(nombres, edades)
}

nombre_input = input("Ingresa un nombre: ")

resultado = buscar_edad(nombre_input, edades)

print(resultado)