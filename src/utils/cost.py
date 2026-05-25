from src.models.finca import Finca


def costo_tablon(
    ts: int,
    tr: int,
    p: int,
    rp: int,
    inicio: int,
) -> int:

    fin = inicio + tr

    # Escenario 1
    if inicio == rp:
        return ts - fin

    # Escenario 2
    if fin <= ts:
        return 2 * (ts - fin)

    # Escenario 3
    return 2 * p * (fin - ts)


def calcular_costo(
    finca: Finca,
    orden: list[int],
) -> int:

    tiempo_actual = 0
    costo_total = 0

    tablones = {
        t.index: t
        for t in finca.tablones
    }

    for idx in orden:

        t = tablones[idx]

        costo_total += costo_tablon(
            ts=t.ts,
            tr=t.tr,
            p=t.p,
            rp=t.rp,
            inicio=tiempo_actual,
        )

        tiempo_actual += t.tr

    return costo_total