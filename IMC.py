def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
    peso <20 or peso > 200:
        return None
    return peso / altura ** 2

print(imc(74, 1.71))

"""

IMC EN PULGADAS

"""
def piespulgam(pies, pulgadas = 0.0):
    return pies * 0.3048 + pulgadas * 0.0254


def lbsakg(lb):
    return lb * 0.45359237


def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None
    
    return peso / altura ** 2


print(imc(peso = lbsakg(176), altura = piespulgam(5, 7)))