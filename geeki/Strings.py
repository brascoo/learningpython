mensaje = "Hola"
mensaje += " "
mensaje += "Ernesto"
print(mensaje)

print("Concatenación:")

mensaje = "Hola"
espacio = " "
nombre = "Ernesto"
print(mensaje + espacio + nombre)

numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("El resultado de la suma es: " + resultado)

print("Busqueda:")

mensaje = "Hola Ernesto"
buscar_subcadena = mensaje.find("Ernesto")
print(buscar_subcadena)

print("Extracción:")

mensaje = "Hola Ernesto"
extraer_cadena = mensaje[1:8]
print(extraer_cadena)

print("Comparación:")

mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)
