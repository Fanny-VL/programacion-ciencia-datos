# Clasificador de Temperaturas - Reto Semana 2
## Fanny Valderrama Lopez - 3AM1

Programa en Python que procesa datos de temperatura por ciudad desde la entrada estándar (stdin), convierte unidades si es necesario y clasifica cada temperatura.

---

## Descripción

El programa recibe líneas en formato:

ciudad,temperatura,unidad

Donde:

- ciudad: nombre de la ciudad
- temperatura: valor numérico
- unidad: C (Celsius) o F (Fahrenheit)

El programa realiza:

1. Validación de datos
2. Conversión de Fahrenheit a Celsius
3. Clasificación de temperatura
4. Impresión del resultado

---

## Clasificación

| Rango (°C) | Clasificación |
|------------|--------------|
| < 15       | Frío |
| 15 - 24.9  | Templado |
| 25 - 34.9  | Cálido |
| ≥ 35       | Caliente |

---

## Ejemplo de Entrada
CDMX,25,C
NewYork,77,F


## Ejemplo de Salida
CDMX,25.0,Cálido
NewYork,25.0,Cálido


---

## Cómo ejecutar

### Windows (PowerShell)
type prueba.txt | python main.py


### Linux / Mac
python main.py < prueba.txt

---

## Requisitos

- Python 3.x

---

## Estructura del proyecto

```
reto-semana-02/
│
├── README.md
├── main.py
└── .gitignore
```
