# el código imprime los valores subsequentes 
# de exp(k), k = 1, 2, 4, 8, 16, ...

def checkNum(promt, high, low):
    if promt <= high and promt >= low:
        print(promt) # devolver el resultado
        return True # Para detener el bucle
    else:
        print('Error: el valor no está dentro del rango permitido ({min}..{max})'.format(min=low,max=high))


def readInt(message):
    while True:
        try:
            num = input(message)

            return int(num) # si el valor no es un número acá ocurrirá un error
        except:
            print('Error: entrada incorrecta')


while True:
    high = readInt('Ingrese el límite superior: ')
    low  = readInt('Ingrese el límite inferior: ')
    num  = readInt('Ingrese el número: ')

    if checkNum(num, high, low):
        break