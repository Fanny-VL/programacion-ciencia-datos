# Sistema de Inventario Modular

## Descripción
Sistema que lee un archivo CSV de inventario, valida los datos y genera un reporte de productos que necesitan reorden (stock menor al mínimo).

---

## Estructura del Proyecto

reto-semana-04/
│── main.py  
│── README.md  
│── .gitignore  
│  
├── models/  
│   ├── __init__.py  
│   └── producto.py   → Clase Producto  
│  
├── utils/  
│   ├── __init__.py  
│   ├── validators.py → Validaciones de datos  
│   └── io.py         → Lectura y escritura de archivos  
│  
├── data/  
│   └── inventario.csv → Archivo de entrada  
│  
└── outputs/  
    └── reporte_inventario.csv → Archivo generado  

---

## Cómo Ejecutar

```bash
python main.py

Entrada

Archivo: data/inventario.csv

Formato:
sku,nombre,categoria,precio,stock,stock_minimo
SKU001,Laptop HP,Electronica,15000.00,5,10

sku: identificador único
nombre: nombre del producto
categoria: categoría
precio: número decimal ≥ 0
stock: entero ≥ 0
stock_minimo: entero ≥ 0

El sistema ignora registros inválidos.

Salida

Archivo: outputs/reporte_inventario.csv

Contiene solo productos que necesitan reorden:
sku,nombre,categoria,stock_actual,stock_minimo,unidades_faltantes,valor_inventario
SKU002,Mouse Logitech,Accesorios,3,15,12,1050.00

Ordenado por unidades faltantes (descendente).

Autor
Valderrama Lopez Fanny.