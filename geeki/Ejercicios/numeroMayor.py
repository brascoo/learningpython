print('#########################################################')
print('# Programa para determinar cúal es el número más grande #')
print('#########################################################\n')

number1 = int(input('Inserta el primer número:'))
number2 = int(input('Inserta el segundo número:'))
number3 = int(input('Inserta el tercer número:'))

if number3 > number2:
    print('El número', number3, 'es el mayor')
elif number2 > number1:
    print('El número', number2, 'es el mayor')
else:
    print('El número', number1, 'es el mayor')

