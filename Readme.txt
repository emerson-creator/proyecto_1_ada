========================================================
PROYECTO 1 - RIEGO ÓPTIMO
Análisis y Diseño de Algoritmos II
========================================================

DESCRIPCIÓN GENERAL
--------------------------------------------------------

Este proyecto implementa una solución para el problema
de Riego Óptimo de una finca utilizando distintos
enfoques algorítmicos:

1. Fuerza Bruta
2. Algoritmo Voraz
3. Programación Dinámica

El objetivo es encontrar el orden óptimo de riego
de los tablones minimizando el costo total asociado
a tiempos, prioridades y penalizaciones.


========================================================
ESTRUCTURA DEL PROYECTO
========================================================
 
proyecto_1_ada/
│
├── main.py
│
├── src/
│   │
│   ├── algorithms/
│   │   ├── fuerza_bruta.py
│   │   ├── programacion_dinamica.py
│   │   └── voraz.py
│   │
│   ├── interface/
│   │   └── gui.py
│   │
│   ├── models/
│   │   ├── finca.py
│   │   ├── resultado.py
│   │   └── tablon.py
│   │
│   └── utils/
│       ├── cost.py
│       ├── formatter.py
│       ├── parser.py
│       └── validator.py
│
├── test/
│   └── archivos de prueba
│
└── output/
    └── resultados generados


========================================================
DESCRIPCIÓN DE LOS ARCHIVOS
========================================================

--------------------------------------------------------
main.py
--------------------------------------------------------

Archivo principal del proyecto.
Ejecuta la interfaz gráfica de usuario.


--------------------------------------------------------
src/algorithms/
--------------------------------------------------------

Contiene la implementación de los algoritmos utilizados
para resolver el problema.

- fuerza_bruta.py
  Implementa búsqueda exhaustiva mediante permutaciones.

- voraz.py
  Implementa una heurística voraz basada en prioridades
  y tiempos.

- programacion_dinamica.py
  Implementa una solución óptima mediante memoización
  y bitmasking.


--------------------------------------------------------
src/interface/
--------------------------------------------------------

Contiene la interfaz gráfica del sistema.

- gui.py
  Implementa la interfaz gráfica utilizando Tkinter.


--------------------------------------------------------
src/models/
--------------------------------------------------------

Define las estructuras principales del sistema.

- finca.py
  Modelo de la finca.

- tablon.py
  Modelo de cada tablón de riego.

- resultado.py
  Modelo del resultado generado por un algoritmo.


--------------------------------------------------------
src/utils/
--------------------------------------------------------

Funciones auxiliares del proyecto.

- parser.py
  Lee archivos de entrada y construye objetos Finca.

- cost.py
  Implementa la función de costo del problema.

- formatter.py
  Imprime y guarda resultados.

- validator.py
  Valida que un orden de riego sea correcto.


--------------------------------------------------------
test/
--------------------------------------------------------

Contiene archivos de prueba de entrada utilizados
para ejecutar los algoritmos.


--------------------------------------------------------
output/
--------------------------------------------------------

Contiene los archivos de salida generados
automáticamente por la aplicación.


========================================================
FORMATO DE LOS ARCHIVOS DE ENTRADA
========================================================

El formato de entrada es:

n
ts,tr,p,rp
ts,tr,p,rp
...

Donde:

- n  : número de tablones
- ts : tiempo sugerido
- tr : tiempo de riego
- p  : prioridad
- rp : tiempo preferido de inicio


--------------------------------------------------------
Ejemplo:
--------------------------------------------------------

5
10,10,1,0
11,2,1,5
13,5,1,7
9,4,4,1
14,1,2,10


========================================================
INSTRUCCIONES DE EJECUCIÓN
========================================================

REQUISITOS
--------------------------------------------------------

- Python 3.10 o superior


--------------------------------------------------------
EJECUCIÓN
--------------------------------------------------------

Ubicarse en la raíz del proyecto y ejecutar:

python main.py


========================================================
FUNCIONAMIENTO DE LA INTERFAZ
========================================================

La interfaz gráfica permite:

- Seleccionar el algoritmo a utilizar.
- Seleccionar un archivo de prueba.
- Ejecutar el algoritmo.
- Visualizar el costo total y el orden óptimo.
- Guardar automáticamente los resultados.


========================================================
RESULTADOS
========================================================

Los resultados se guardan automáticamente en la carpeta:

output/

con nombres del tipo:

test1_out.txt


========================================================
ALGORITMOS IMPLEMENTADOS
========================================================

--------------------------------------------------------
1. Fuerza Bruta
--------------------------------------------------------

Explora todas las permutaciones posibles para encontrar
la solución óptima.

Complejidad aproximada:

O(n!)


--------------------------------------------------------
2. Algoritmo Voraz
--------------------------------------------------------

Utiliza una heurística basada en:
- margen de inicio,
- prioridad,
- tiempo de riego.

Complejidad aproximada:

O(n log n)


--------------------------------------------------------
3. Programación Dinámica
--------------------------------------------------------

Utiliza memoización y bitmasking para reducir
la cantidad de estados recalculados.

Complejidad aproximada:

O(2^n * n)


========================================================
AUTORES
========================================================

Proyecto desarrollado para el curso:

Análisis y Diseño de Algoritmos II

Universidad del Valle