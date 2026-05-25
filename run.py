import sys

from src.algorithms.fuerza_bruta import roFB
from src.algorithms.voraz import roV

from src.utils.parser import leer_finca


def main():

    algoritmo = sys.argv[1]
    archivo = sys.argv[2]

    finca = leer_finca(archivo)

    if algoritmo == "fb":
        resultado = roFB(finca)

    elif algoritmo == "voraz":
        resultado = roV(finca)

    else:
        raise ValueError(
            "Algoritmo inválido"
        )

    print(resultado)


if __name__ == "__main__":
    main()