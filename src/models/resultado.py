from dataclasses import dataclass


@dataclass
class Resultado:
    orden: list[int]
    costo: int