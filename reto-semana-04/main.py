from models import Producto
from utils import validar_producto, leer_inventario, escribir_reporte

# Rutas
ARCHIVO_INVENTARIO = "data/inventario.csv"
ARCHIVO_REPORTE = "outputs/reporte_inventario.csv"


def crear_productos(datos_raw):
    productos = []

    for datos in datos_raw:

        es_valido, error = validar_producto(
            datos.get("sku"),
            datos.get("nombre"),
            datos.get("categoria"),
            datos.get("precio"),
            datos.get("stock"),
            datos.get("stock_minimo"),
        )

        if not es_valido:
            print(f"[IGNORADO] {error}")
            continue

        producto = Producto(
            sku=datos["sku"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=float(datos["precio"]),
            stock=int(datos["stock"]),
            stock_minimo=int(datos["stock_minimo"]),
        )

        productos.append(producto)

    return productos


def filtrar_necesitan_reorden(productos):
    return [p for p in productos if p.necesita_reorden()]


def ordenar_por_faltantes(productos):
    return sorted(productos, key=lambda p: p.unidades_faltantes(), reverse=True)


def main():
    print("=" * 50)
    print("SISTEMA DE INVENTARIO - REPORTE DE REORDEN")
    print("=" * 50)

    # 1. Leer CSV
    datos_raw = leer_inventario(ARCHIVO_INVENTARIO)
    print(f"Registros leídos: {len(datos_raw)}")

    # 2. Crear objetos válidos
    productos = crear_productos(datos_raw)
    print(f"Productos válidos: {len(productos)}")

    # 3. Filtrar
    necesitan_reorden = filtrar_necesitan_reorden(productos)
    print(f"Necesitan reorden: {len(necesitan_reorden)}")

    # 4. Ordenar
    necesitan_reorden = ordenar_por_faltantes(necesitan_reorden)

    # 5. Mostrar resultados
    print("\n--- PRODUCTOS A REORDENAR ---")
    for p in necesitan_reorden:
        print(p)

    # 6. Guardar reporte
    escribir_reporte(necesitan_reorden, ARCHIVO_REPORTE)
    print(f"\nReporte generado en: {ARCHIVO_REPORTE}")

    print("\nProceso terminado correctamente")


if __name__ == "__main__":
    main()