# Analizador de Ventas - Reto Semana 3

## Valderrama Lopez Fanny - 3AM1

Programa en Python que procesa un archivo CSV desde la entrada estándar (stdin), agrupa transacciones por producto y calcula métricas de ventas.

---

## Descripción

El programa analiza registros de ventas y genera un reporte consolidado por producto.

Para cada producto calcula:

* Unidades vendidas
* Ingreso total
* Precio promedio

El resultado se ordena de mayor a menor ingreso total.

---

## Formato de Entrada

El programa recibe un archivo CSV desde stdin con el siguiente formato:

```
fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,10,250.00
```

### Reglas:

* La primera línea es encabezado (se ignora)
* Cada línea representa una transacción
* Las columnas deben ser 4
* Si hay datos inválidos, la línea se ignora

---

## Formato de Salida

El programa imprime un CSV con el siguiente formato:

```
producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,3,44500.00,14833.33
Mouse,18,4500.00,250.00
```

### Reglas:

* Ordenado por ingreso total (descendente)
* Unidades: enteros
* Valores monetarios: 2 decimales
* Sin texto adicional

---

## Ejemplo

### Entrada:

```
fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,10,250.00
2026-01-03,Laptop,1,14500.00
2026-01-04,Teclado,5,800.00
2026-01-05,Mouse,8,250.00
```

### Salida:

```
producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,3,44500.00,14833.33
Mouse,18,4500.00,250.00
Teclado,5,4000.00,800.00
```

---

## Cómo ejecutar

### En Windows (PowerShell)

```
type tests\entrada1.txt | python main.py
```

### En Linux / Mac

```
python main.py < tests/entrada1.txt
```

---

## Estructura del proyecto

```
reto-semana-03/
│
├── main.py
├── README.md
├── .gitignore
└── tests/
    ├── entrada1.txt
    └── salida1.txt
```

---

## Requisitos

* Python 3.x

---

## Notas

* El programa ignora líneas inválidas automáticamente
* Maneja errores con try/except
* Utiliza diccionarios para agrupar datos
