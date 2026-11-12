import math

def calcular_potencia(base, exponente):
    return base ** exponente

def calcular_modulo(a, b):
    if b == 0:
        raise ValueError("Error: División o módulo con divisor cero.")
    return a % b

def calcular_raiz_cuadrada(n):
    if n < 0:
        raise ValueError("Error: No se acepta raíz cuadrada de valores negativos.")
    return math.sqrt(n)

def calcular_porcentaje(cantidad, porcentaje):
    return (cantidad * porcentaje) / 100

def calcular_valor_absoluto(n):
    return abs(n)
def calcular_factorial(n):
    if n < 0 or not isinstance(n, int):
        raise ValueError("Error: El factorial requiere un entero no negativo.")
    return math.factorial(n)

def calcular_promedio(lista_numeros):
    if not lista_numeros:
        raise ValueError("Error: La lista de números está vacía.")
    return sum(lista_numeros) / len(lista_numeros)

def calcular_redondeo(valor, decimales):
    return round(valor, decimales)