# Calculadora de Sumas - Reto Semana 1
## Valderrama Lopez Fanny - 3AM1

Programa en Python que procesa líneas de texto con números separados por comas, limpia los datos y calcula la suma total por cada línea.



## Descripción

El programa lee datos desde la entrada estándar (stdin) línea por línea.

Cada línea puede contener:

- Números enteros
- Números decimales
- Caracteres no válidos
- Espacios adicionales
- Valores negativos
- Líneas vacías

El procesamiento se realiza siguiendo estas reglas:

1. Las líneas vacías devuelven 0.
2. Se eliminan caracteres no válidos (solo se permiten dígitos, punto y signo negativo).
3. Los números decimales se truncan a enteros usando `int()`.
4. Se suman todos los valores de la línea.
5. Se imprime el resultado para cada línea.



### Ejemplo de Entrada

```
1,2,3
10

1.9,2.1,3.7
1a2,3b,4
-5,10,3
  5 , 10 , 15
0,0,0
-1,-2,-3
abc,def
3.99
-0.5,0.5
,1,2,
100
```

### Ejemplo de Salida

```
6
10
6
8
8
30
0
-6
0
3
0
3
100
```



## Cómo ejecutar el programa

### En Windows (PowerShell)

type prueba.txt | python main.py


### En Linux o Mac

python main.py < prueba.txt


También se puede ejecutar manualmente:

python main.py


---

## Requisitos

- Python 3.x

---

## Estructura del proyecto

```
reto-semana-01/
│
├── .gitignore
├── README.md
└── main.py
```

