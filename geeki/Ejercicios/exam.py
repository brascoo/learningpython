print('***************************************')
print('* Sistema de control vacacional Rappi *')
print('***************************************\n')
nombre = input('Ingresa tu nombre:')
claveDepartamento = int(input('Ingresa tu clave de departamento:'))
antiguedad = float(input('Ingresa tu antiguedad en años:'))

if claveDepartamento == 1:
    if antiguedad <= 1:
        print(nombre, 'Tienes 6 días de vacaciones')
    elif antiguedad > 1 and antiguedad <= 6:
        print (nombre, 'Tienes 14 días de vacaciones')
    else:
        print (nombre, 'Tienes 20 días de vacaciones')
elif claveDepartamento == 2:
    if antiguedad <= 1:
        print(nombre, 'Tienes 7 días de vacaciones')
    elif antiguedad > 1 and antiguedad <= 6:
        print (nombre, 'Tienes 15 días de vacaciones')
    else:
        print (nombre, 'Tienes 22 días de vacaciones')
elif claveDepartamento == 3:
    if antiguedad <= 1:
        print(nombre, 'Tienes 10 días de vacaciones')
    elif antiguedad > 1 and antiguedad <= 6:
        print (nombre, 'Tienes 20 días de vacaciones')
    else:
        print (nombre, 'Tienes 30 días de vacaciones')
else:
    print('Esta clave de departamento no existe')

