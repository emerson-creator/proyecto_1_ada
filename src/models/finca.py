from dataclasses import dataclass
from typing import List

from .tablon import Tablon


@dataclass
class Finca:
    tablones: List[Tablon]

    @property
    def n(self) -> int:
        return len(self.tablones)