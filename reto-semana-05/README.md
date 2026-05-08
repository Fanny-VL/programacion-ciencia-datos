# Perfilador de Datos CSV

## Descripción

Este programa analiza un archivo CSV y genera un perfil de cada columna, incluyendo tipo de dato, valores nulos, valores únicos y porcentajes.

---

## Requisitos

* Python 3.8 o superior

---

## Ejecución

```bash
python main.py --input data/ventas.csv --output outputs/perfil.csv
```

---

## Formato de entrada

Archivo CSV con encabezados en la primera fila.

Ejemplo:

```csv
fecha,producto,cantidad,precio,vendedor
2026-01-01,Laptop,2,15000.00,Ana
```

---

## Formato de salida

El programa genera un CSV con:

* nombre_columna
* tipo_inferido
* total_registros
* valores_nulos
* porcentaje_nulos
* valores_unicos
* porcentaje_unicos
* ejemplo_valor

---

## Estructura del proyecto

```
reto-semana-05/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── ventas.csv
│
└── outputs/
    └── perfil.csv
```

---

## Autor

Valderrama Lopez Fanny