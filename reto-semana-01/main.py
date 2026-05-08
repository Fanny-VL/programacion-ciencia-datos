import sys


def limpiar_valor(valor):
    """
    Elimina espacios y caracteres inválidos de un valor.
    Solo permite dígitos, punto y signo negativo.
    """
    valor = valor.strip()
    caracteres_validos = "0123456789.-"
    limpio = ""

    for char in valor:
        if char in caracteres_validos:
            limpio += char

    return limpio


def convertir_a_entero(texto):
    """
    Convierte un texto a entero truncando decimales.
    Si no es convertible, retorna 0.
    """
    if texto == "":
        return 0

    try:
        numero = float(texto)
        return int(numero)  # Truncar hacia cero
    except ValueError:
        return 0


def procesar_linea(linea):
    """
    Procesa una línea completa:
    - Si está vacía → retorna 0
    - Separa por comas
    - Limpia cada valor
    - Convierte y suma
    """
    linea = linea.strip()

    if linea == "":
        return 0

    valores = linea.split(",")
    suma = 0

    for valor in valores:
        limpio = limpiar_valor(valor)
        numero = convertir_a_entero(limpio)
        suma += numero

    return suma


def main():
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)


if __name__ == "__main__":
    main()