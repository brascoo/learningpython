año = int(input("Introduzca un año:"))

if año <= 1582:
    print("No dentro del periodo del calendario gregoriano")
elif año % 4 != 0: 
    print("año común")
elif año % 100 != 0:
    print("año bisiesto")
elif año % 400 !=0:
    print("año común")
else:
    print("año bisiesto")