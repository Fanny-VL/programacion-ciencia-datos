def leer_inventario(ruta_archivo):
    productos = []

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        if not lineas:
            return productos

        encabezados = lineas[0].strip().split(",")

        for linea in lineas[1:]:
            linea = linea.strip()

            if not linea:
                continue

            valores = linea.split(",")

            if len(valores) != len(encabezados):
                # Ignorar líneas con columnas incorrectas
                continue

            producto_dict = dict(zip(encabezados, valores))
            productos.append(producto_dict)

    return productos


def escribir_reporte(productos, ruta_archivo):

    encabezados = [
        "sku",
        "nombre",
        "categoria",
        "stock_actual",
        "stock_minimo",
        "unidades_faltantes",
        "valor_inventario",
    ]

    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(",".join(encabezados) + "\n")

        for p in productos:
            linea = (
                f"{p.sku},{p.nombre},{p.categoria},{p.stock},"
                f"{p.stock_minimo},{p.unidades_faltantes()},"
                f"{p.valor_inventario():.2f}"
            )
            archivo.write(linea + "\n")