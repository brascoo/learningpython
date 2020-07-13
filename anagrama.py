palabra1 = input("Inserta una palabra: ").upper()
palabra2 = input("Inserta otra palabra: ").upper()

a = list(palabra1)
b = list(palabra2)

palabra1 = a.sort()
palabra2 = b.sort()
    
if palabra1 == [] and palabra2 == []:
    print("No es un anagrama")
elif palabra1 == palabra2:
    print("Es un anagrama")
else:
    print("No es un anagrama")
print(ord(a[0]),ord(b[0]))