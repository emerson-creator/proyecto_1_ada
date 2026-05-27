from src.models.finca import Finca
from src.models.resultado import Resultado

from src.utils.cost import calcular_costo


def roV(finca: Finca) -> Resultado:

    tablones_ordenados = sorted(
        finca.tablones,
        key=lambda t: (
            t.ts - t.tr,  # menor margen de inicio primero
            -t.p,         # mayor prioridad primero (se niega para ordenar desc)
            t.tr,         # menor tiempo de riego primero
        )
    )

    orden = [
        t.index
        for t in tablones_ordenados
    ]

    costo = calcular_costo(
        finca,
        orden,
    )

    return Resultado(
        orden=orden,
        costo=costo,
    )