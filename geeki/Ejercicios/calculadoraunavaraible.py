print('Esto es una calculadora con una sola variable\n')
print('####################')
print('# Menú de opciones #')
print('####################\n')

print('1.Suma')
print('2.Resta')
print('3.Multiplicación')
print('4.División\n')

opcion = int(input('Introduce la opción deseada:'))
numero = int(input('Introduce el primer número:'))

if opcion == 1:
    numero += int(input('Introduce el segundo número:'))
    print('El resultado de la suma es:', numero)
elif opcion == 2:
    numero -= int(input('introduce el segundo número:'))
    print('El resultado de la resta es:', numero)
elif opcion == 3:
    numero *= int(input('introduce el segundo número:'))
    print('El resultado de la multiplicación es:', numero)
elif opcion == 4:
    numero /= int(input('introduce el segundo número:'))
    print('El resultado de la división es:', numero)
else:
    print('La opción seleccionada no existe.')


