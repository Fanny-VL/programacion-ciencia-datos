import argparse
import sys


# ---------------------------
# VALIDACIONES
# ---------------------------

def es_valor_nulo(valor):
    if valor is None:
        return True
    if isinstance(valor, str) and valor.strip() == "":
        return True
    return False


def es_numerico(valor):
    try:
        float(str(valor).replace(",", "").strip())
        return True
    except:
        return False


def es_fecha(valor):
    v = str(valor).strip()
    if len(v) >= 10 and v[4] == "-" and v[7] == "-":
        try:
            y, m, d = map(int, v[:10].split("-"))
            return 1900 <= y <= 2100 and 1 <= m <= 12 and 1 <= d <= 31
        except:
            return False
    return False


def es_booleano(valor):
    v = str(valor).strip().lower()
    return v in ["true", "false", "yes", "no", "si", "1", "0", "t", "f"]


# ---------------------------
# INFERENCIA
# ---------------------------

def inferir_tipo(valores):
    validos = [v for v in valores if not es_valor_nulo(v)]

    if not validos:
        return "texto"

    total = len(validos)
    umbral = 0.8

    num = sum(es_numerico(v) for v in validos)
    fecha = sum(es_fecha(v) for v in validos)
    booleano = sum(es_booleano(v) for v in validos)

    if fecha / total >= umbral:
        return "fecha"
    elif booleano / total >= umbral:
        return "booleano"
    elif num / total >= umbral:
        return "numerico"
    else:
        return "texto"


# ---------------------------
# PERFILADOR
# ---------------------------

def perfilar_columna(nombre, valores):
    total = len(valores)
    nulos = sum(es_valor_nulo(v) for v in valores)

    no_nulos = [v for v in valores if not es_valor_nulo(v)]
    unicos = len(set(no_nulos))
    ejemplo = no_nulos[0] if no_nulos else ""

    tipo = inferir_tipo(valores)

    pct_nulos = round((nulos / total) * 100, 2) if total else 0.0
    pct_unicos = round((unicos / total) * 100, 2) if total else 0.0

    return {
        "nombre_columna": nombre,
        "tipo_inferido": tipo,
        "total_registros": total,
        "valores_nulos": nulos,
        "porcentaje_nulos": pct_nulos,
        "valores_unicos": unicos,
        "porcentaje_unicos": pct_unicos,
        "ejemplo_valor": ejemplo
    }


# ---------------------------
# CSV
# ---------------------------

def leer_csv(ruta):
    with open(ruta, encoding="utf-8") as f:
        lineas = f.readlines()

    if not lineas:
        return [], []

    encabezados = lineas[0].strip().split(",")
    filas = [l.strip().split(",") for l in lineas[1:] if l.strip()]

    return encabezados, filas


def escribir_csv(ruta, perfiles):
    columnas = [
        "nombre_columna", "tipo_inferido", "total_registros",
        "valores_nulos", "porcentaje_nulos",
        "valores_unicos", "porcentaje_unicos", "ejemplo_valor"
    ]

    with open(ruta, "w", encoding="utf-8") as f:
        f.write(",".join(columnas) + "\n")

        for p in perfiles:
            fila = [
                str(p["nombre_columna"]),
                str(p["tipo_inferido"]),
                str(p["total_registros"]),
                str(p["valores_nulos"]),
                f"{p['porcentaje_nulos']:.2f}",
                str(p["valores_unicos"]),
                f"{p['porcentaje_unicos']:.2f}",
                str(p["ejemplo_valor"])
            ]
            f.write(",".join(fila) + "\n")


# ---------------------------
# MAIN
# ---------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", required=True)
    parser.add_argument("--output", "-o", required=True)

    args = parser.parse_args()

    try:
        encabezados, filas = leer_csv(args.input)
    except FileNotFoundError:
        print("Archivo no encontrado")
        sys.exit(1)

    if not encabezados:
        print("CSV vacío")
        sys.exit(1)

    perfiles = []

    for i, col in enumerate(encabezados):
        valores = [fila[i] if i < len(fila) else "" for fila in filas]
        perfiles.append(perfilar_columna(col, valores))

    escribir_csv(args.output, perfiles)

    print("Perfil generado correctamente")


if __name__ == "__main__":
    main()