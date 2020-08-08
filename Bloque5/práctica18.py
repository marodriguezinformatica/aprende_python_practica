import math

def suma(c1,c2):
    result = c1 + c2
    return result

def resta(c1,c2):
    result = c1 - c2
    return result

def multiplicacion(c1,c2):
    result = c1 * c2
    return result

def dividir(c1,c2):
    result = c1 / c2
    return result

def modulo(c1):
    result = math.sqrt(math.pow(c1.real,2)+math.pow(c1.imag,2))
    return result

def argumento(c1):
    result = math.atan(c1.imag/c1.real)
    return result

def opuesto(c1):
    result = complex(-c1.real,-c1.imag)
    return result

def conjugado(c1):
    result = complex(c1.real,-c1.imag)
    return result