digit =[[
'###',
'# #',
'# #',
'# #',
'###',
],
[
'  #',
'  #',
'  #',
'  #',
'  #',
],
[
'###',
'  #',
'###',
'#  ',
'###',
],
[
'###',
'  #',
'###',
'  #',
'###',
],
[
'# #',
'# #',
'###',
'  #',
'  #',
],
[
'###',
'#  ',
'###',
'  #',
'###',
],
[
'###',
'#  ',
'###',
'# #',
'###',
],
[
'###',
'  #',
'  #',
'  #',
'  #',
],
[
'###',
'# #',
'###',
'# #',
'###',
],
[
'###',
'# #',
'###',
'  #',
'###',
]]

print(digit[0][0] + ' ' + digit[1][0] + ' ' + digit[2][0])
print(digit[0][1] + ' ' + digit[1][1] + ' ' + digit[2][1])
print(digit[0][2] + ' ' + digit[1][2] + ' ' + digit[2][2])
print(digit[0][3] + ' ' + digit[1][3] + ' ' + digit[2][3])
print(digit[0][4] + ' ' + digit[1][4] + ' ' + digit[2][4])

"""para cada renglón de 0 a 4 (son 5):
  renglon = "" 
  para cada digito del numero:
     concatenar al renglón el elemento digitos[digito][renglon]
     concatenar al renglón un espacio en blando
  imprimir renglón
"""
numero = int(input("ingresa un numero:"))
x = int(len(numero))
for i in range(5):
    renglon = ""
    
    for cifra in range(x):
        renglon = (digit[numero][i] + " " + digit[cifra][i])
    
    print(renglon)
