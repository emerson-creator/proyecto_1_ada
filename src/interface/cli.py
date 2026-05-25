from src.algorithms.fuerza_bruta import roFB
from src.algorithms.voraz import roV

from src.utils.formatter import (
    imprimir_resultado,
)

from src.utils.parser import leer_finca


def iniciar_cli():

    path = input(
        "\nRuta archivo entrada: "
    )

    finca = leer_finca(path)

    print("\nSeleccione algoritmo:")
    print("1. Fuerza Bruta")
    print("2. Voraz")

    opcion = input("> ")

    if opcion == "1":
        resultado = roFB(finca)

    elif opcion == "2":
        resultado = roV(finca)

    else:
        print("Opción inválida")
        return

    imprimir_resultado(resultado)