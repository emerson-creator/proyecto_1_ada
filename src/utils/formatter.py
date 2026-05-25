from pathlib import Path

from src.models.resultado import Resultado


def imprimir_resultado(resultado: Resultado):

    print(f"\nCosto total: {resultado.costo}")

    print("\nOrden de riego:")

    for idx in resultado.orden:
        print(idx)


def guardar_resultado(
    resultado: Resultado,
    output_path: str,
):

    path = Path(output_path)

    contenido = [str(resultado.costo)]

    contenido.extend(
        str(i)
        for i in resultado.orden
    )

    path.write_text(
        "\n".join(contenido),
        encoding="utf-8",
    )