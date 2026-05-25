from pathlib import Path

from src.models.finca import Finca
from src.models.tablon import Tablon


def leer_finca(path: str) -> Finca:
    archivo = Path(path)

    lineas = [
        linea.strip()
        for linea in archivo.read_text(encoding="utf-8").splitlines()
        if linea.strip()
    ]

    n = int(lineas[0])

    tablones = []

    for i, linea in enumerate(lineas[1:]):
        ts, tr, p, rp = map(int, linea.split(","))

        tablones.append(
            Tablon(
                index=i,
                ts=ts,
                tr=tr,
                p=p,
                rp=rp,
            )
        )

    return Finca(tablones)