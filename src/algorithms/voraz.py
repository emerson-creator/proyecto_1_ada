from itertools import permutations

from src.models.finca import Finca
from src.models.resultado import Resultado

from src.utils.cost import calcular_costo


def roFB(finca: Finca) -> Resultado:

    ids = [
        t.index
        for t in finca.tablones
    ]

    mejor_orden = None
    mejor_costo = float("inf")

    for perm in permutations(ids):

        orden = list(perm)

        costo = calcular_costo(
            finca,
            orden,
        )

        if costo < mejor_costo:

            mejor_costo = costo
            mejor_orden = orden

    return Resultado(
        orden=mejor_orden,
        costo=mejor_costo,
    )