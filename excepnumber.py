#!5.1.6.4

def readint(prompt, min, max):
    
    try:
        prompt = int(input('Ingresa un numero de -10 a 10: '))
        min = -10
        max = 10
        if prompt >= min and prompt <= max:
            return prompt
                
    except ValueError:
        print('Error: entrada incorrecta')
        readint(prompt,min,max)
    #except TypeError:
    #    print('Error: el valor no está dentro del rango permitido (-10..10)')
    #    readint(prompt,min,max)

v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)