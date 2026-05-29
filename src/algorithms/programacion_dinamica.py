from functools import lru_cache

from src.models.finca import Finca
from src.models.resultado import Resultado


def roPD(finca: Finca) -> Resultado:
    from functools import lru_cache

from src.models.finca import Finca
from src.models.resultado import Resultado

from src.utils.cost import costo_tablon


def roPD(finca: Finca) -> Resultado:

    tablones = finca.tablones

    n = finca.n

    # Máscara completa:
    # Ejemplo n=5 → 11111
    FULL_MASK = (1 << n) - 1

    @lru_cache(maxsize=None)
    def dp(mask: int, tiempo_actual: int):

        # =====================================
        # CASO BASE
        # =====================================

        if mask == 0:
            return 0, []

        mejor_costo = float("inf")

        mejor_orden = []

        # =====================================
        # PROBAR CADA TABLÓN DISPONIBLE
        # =====================================

        for i in range(n):

            # Verificar si el tablón i
            # sigue disponible en la máscara
            if mask & (1 << i):

                t = tablones[i]

                # ---------------------------------
                # Costo de ejecutar este tablón
                # en el tiempo actual
                # ---------------------------------

                costo_actual = costo_tablon(
                    ts=t.ts,
                    tr=t.tr,
                    p=t.p,
                    rp=t.rp,
                    inicio=tiempo_actual,
                )

                # ---------------------------------
                # Eliminar tablón i de la máscara
                # ---------------------------------

                nuevo_mask = mask ^ (1 << i)

                # ---------------------------------
                # Resolver subproblema restante
                # ---------------------------------

                costo_restante, orden_restante = dp(
                    nuevo_mask,
                    tiempo_actual + t.tr
                )

                costo_total = (
                    costo_actual
                    + costo_restante
                )

                # ---------------------------------
                # Actualizar mejor solución
                # ---------------------------------

                if costo_total < mejor_costo:

                    mejor_costo = costo_total

                    mejor_orden = (
                        [i]
                        + orden_restante
                    )

        return mejor_costo, mejor_orden

    # =========================================
    # RESOLVER PROBLEMA COMPLETO
    # =========================================

    costo_optimo, orden_optimo = dp(
        FULL_MASK,
        0
    )

    return Resultado(
        orden=orden_optimo,
        costo=costo_optimo,
    )