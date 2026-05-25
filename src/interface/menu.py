from dataclasses import dataclass


@dataclass(frozen=True)
class Tablon:
    index: int
    ts: int
    tr: int
    p: int
    rp: int