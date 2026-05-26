import sys
from datetime import datetime


def fecha_valida(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def main():
    productos = {}
    primera_linea = True

    for linea in sys.stdin:
        linea = linea.strip()

        # Saltar encabezado
        if primera_linea:
            primera_linea = False
            continue

        if not linea:
            continue

        partes = linea.split(",")

        # Validar columnas
        if len(partes) != 4:
            continue

        fecha = partes[0].strip()
        producto = partes[1].strip()

        # Validar fecha
        if not fecha_valida(fecha):
            continue

        # Validar producto no vacío
        if producto == "":
            continue

        try:
            cantidad = int(partes[2])
            precio = float(partes[3])

            # Validar positivos
            if cantidad <= 0 or precio <= 0:
                continue

        except ValueError:
            continue

        # Crear producto si no existe
        if producto not in productos:
            productos[producto] = {
                "unidades": 0,
                "ingreso": 0.0
            }

        # Acumular
        productos[producto]["unidades"] += cantidad
        productos[producto]["ingreso"] += cantidad * precio

    # Calcular promedios
    for prod in productos:
        unidades = productos[prod]["unidades"]
        ingreso = productos[prod]["ingreso"]

        productos[prod]["promedio"] = ingreso / unidades

    # Ordenar por ingreso descendente
    productos_ordenados = sorted(
        productos.items(),
        key=lambda x: x[1]["ingreso"],
        reverse=True
    )

    # Salida exacta
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")

    for nombre, datos in productos_ordenados:
        print(
            f"{nombre},"
            f"{datos['unidades']},"
            f"{datos['ingreso']:.2f},"
            f"{datos['promedio']:.2f}"
        )


if __name__ == "__main__":
    main()