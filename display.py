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

numero = input("ingresa un numero:")

for i in range(5):
    renglon = ""
    for cifra in numero:
      cifra = int(cifra)
      renglon += digit[cifra][i]
      renglon += " "
    
    print(renglon)
