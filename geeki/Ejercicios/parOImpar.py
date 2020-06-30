print('********************************************************')
print("** Este Programa determina si un número es par o impar **")
print('********************************************************\n')

numero = int(input('Por favor ingresa un número entero:'))

if numero % 2 == 0:
    print('\nEl número', numero, 'es par')
else:
    print('\nEl número', numero, 'es impar')