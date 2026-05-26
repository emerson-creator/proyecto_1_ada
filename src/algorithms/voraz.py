from src.models.finca import Finca
from src.models.resultado import Resultado

from src.utils.cost import calcular_costo


def roV(finca: Finca) -> Resultado:

    tablones_ordenados = sorted(
        finca.tablones,
        key=lambda t: (
            t.ts - t.tr,
            -t.p,
            t.tr,
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