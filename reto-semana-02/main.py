import sys


def clasificar(temp):
    if temp < 15:
        return "Frío"
    elif temp < 25:
        return "Templado"
    elif temp < 35:
        return "Cálido"
    else:
        return "Caliente"


def main():
    for linea in sys.stdin:
        linea = linea.strip()

        partes = linea.split(",")

        if len(partes) != 3:
            continue

        ciudad = partes[0]
        temp_str = partes[1]
        unidad = partes[2]

        try:
            temperatura = float(temp_str)
        except ValueError:
            continue

        if unidad not in ["C", "F"]:
            continue

        # Convertir a Celsius
        if unidad == "F":
            temperatura = (temperatura - 32) * 5 / 9

        # Clasificar
        clasificacion = clasificar(temperatura)

        print(f"{ciudad},{temperatura:.1f},{clasificacion}")


if __name__ == "__main__":
    main()