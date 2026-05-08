import sys


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

        if len(partes) != 4:
            continue

        producto = partes[1]

        try:
            cantidad = int(partes[2])
            precio = float(partes[3])
        except ValueError:
            continue

        # Crear si no existe
        if producto not in productos:
            productos[producto] = {
                "unidades": 0,
                "ingreso": 0.0
            }

        # Acumular
        productos[producto]["unidades"] += cantidad
        productos[producto]["ingreso"] += cantidad * precio

    # Calcular promedio
    for prod in productos:
        unidades = productos[prod]["unidades"]
        ingreso = productos[prod]["ingreso"]
        productos[prod]["promedio"] = ingreso / unidades if unidades > 0 else 0

    # Ordenar
    productos_ordenados = sorted(
        productos.items(),
        key=lambda x: x[1]["ingreso"],
        reverse=True
    )

    # Imprimir salida
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")

    for nombre, datos in productos_ordenados:
        print(f"{nombre},{datos['unidades']},{datos['ingreso']:.2f},{datos['promedio']:.2f}")


if __name__ == "__main__":
    main()