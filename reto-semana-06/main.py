import re
from typing import Dict, List

# Departamentos válidos
DEPARTAMENTOS_VALIDOS = ['VEN', 'ADM', 'TEC', 'LOG', 'RRH']

# Series válidas
SERIES_VALIDAS = ['A', 'B', 'C', 'D', 'E']


# =========================
# VALIDADORES INDIVIDUALES
# =========================

def validar_producto(codigo: str) -> Dict:
    resultado = {
        "valido": False,
        "categoria": None,
        "numero": None,
        "pais": None
    }

    patron = r'^([A-Z]{3})-(\d{4})-([A-Z]{2})$'

    match = re.match(patron, codigo)

    if match:
        resultado["valido"] = True
        resultado["categoria"] = match.group(1)
        resultado["numero"] = match.group(2)
        resultado["pais"] = match.group(3)

    return resultado


def validar_envio(codigo: str) -> Dict:
    resultado = {
        "valido": False,
        "fecha": None,
        "secuencial": None
    }

    patron = r'^ENV-(20[2-3][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{6})$'

    match = re.match(patron, codigo)

    if match:
        resultado["valido"] = True
        resultado["fecha"] = f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
        resultado["secuencial"] = match.group(4)

    return resultado


def validar_empleado(codigo: str) -> Dict:
    resultado = {
        "valido": False,
        "departamento": None,
        "numero": None
    }

    patron = r'^EMP-([A-Z]{3})-([1-9]\d{3})$'

    match = re.match(patron, codigo)

    if match:
        departamento = match.group(1)

        if departamento in DEPARTAMENTOS_VALIDOS:
            resultado["valido"] = True
            resultado["departamento"] = departamento
            resultado["numero"] = match.group(2)

    return resultado


def validar_factura(codigo: str) -> Dict:
    resultado = {
        "valido": False,
        "serie": None,
        "numero": None
    }

    patron = r'^FAC-([A-E])-(\d{6})$'

    match = re.match(patron, codigo)

    if match:
        serie = match.group(1)

        if serie in SERIES_VALIDAS:
            resultado["valido"] = True
            resultado["serie"] = serie
            resultado["numero"] = match.group(2)

    return resultado


# =========================
# VALIDADOR UNIVERSAL
# =========================

def validar_codigo(codigo: str) -> Dict:
    resultado = {
        "codigo": codigo,
        "tipo": "desconocido",
        "valido": False,
        "detalles": {}
    }

    if codigo.startswith("ENV"):
        resultado["tipo"] = "envio"
        detalles = validar_envio(codigo)

    elif codigo.startswith("EMP"):
        resultado["tipo"] = "empleado"
        detalles = validar_empleado(codigo)

    elif codigo.startswith("FAC"):
        resultado["tipo"] = "factura"
        detalles = validar_factura(codigo)

    elif re.match(r'^[A-Z]{3}-', codigo):
        resultado["tipo"] = "producto"
        detalles = validar_producto(codigo)

    else:
        detalles = {}

    if detalles:
        resultado["valido"] = detalles["valido"]
        resultado["detalles"] = detalles

    return resultado


# =========================
# PROCESAMIENTO POR LOTES
# =========================

def procesar_lote(codigos: List[str]) -> Dict:
    resultado = {
        "total": 0,
        "validos": 0,
        "invalidos": 0,
        "por_tipo": {
            "producto": {"total": 0, "validos": 0},
            "envio": {"total": 0, "validos": 0},
            "empleado": {"total": 0, "validos": 0},
            "factura": {"total": 0, "validos": 0},
            "desconocido": {"total": 0, "validos": 0}
        },
        "detalle": []
    }

    for codigo in codigos:
        res = validar_codigo(codigo)

        resultado["detalle"].append(res)
        resultado["total"] += 1

        tipo = res["tipo"]

        resultado["por_tipo"][tipo]["total"] += 1

        if res["valido"]:
            resultado["validos"] += 1
            resultado["por_tipo"][tipo]["validos"] += 1
        else:
            resultado["invalidos"] += 1

    return resultado


# =========================
# FUNCIONES DE REPORTE
# =========================

def mostrar_resultado(resultado: Dict) -> None:
    estado = "✓" if resultado["valido"] else "X"

    print(f"{estado} {resultado['codigo']:<30} | Tipo: {resultado['tipo']}")


def mostrar_reporte(reporte: Dict) -> None:
    print("=" * 60)
    print("               REPORTE DE VALIDACIÓN")
    print("=" * 60)

    print(f"\nTotal procesados: {reporte['total']}")
    print(f"Válidos: {reporte['validos']}")
    print(f"Inválidos: {reporte['invalidos']}")

    print("\nDesglose por tipo:")

    for tipo, datos in reporte["por_tipo"].items():
        print(f"{tipo}: {datos}")

    print("=" * 60)


# =========================
# DATOS DE PRUEBA
# =========================

CODIGOS_PRUEBA = [
    "TEC-0001-MX",
    "tec-0001-MX",
    "ENV-2024-03-15-001234",
    "ENV-2024-13-15-001234",
    "EMP-VEN-1234",
    "EMP-XXX-1234",
    "FAC-A-123456",
    "FAC-F-123456",
    "RANDOM-CODE",
    "ALI-9999-US"
]


# =========================
# PRUEBAS
# =========================

print("PRUEBA DE VALIDACIONES")
print("=" * 50)

for codigo in CODIGOS_PRUEBA:
    resultado = validar_codigo(codigo)
    mostrar_resultado(resultado)

print("\n")
print("=" * 50)

reporte = procesar_lote(CODIGOS_PRUEBA)
mostrar_reporte(reporte)