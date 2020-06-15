miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista[0]

for i in range(1, len(miLista)):
   if miLista [i]> mayor:
        mayor = miLista[i]

print(mayor)

----------------------------------
miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista [0]

for i in miLista [1:]:
   if i > mayor:
        mayor = i

print(mayor)