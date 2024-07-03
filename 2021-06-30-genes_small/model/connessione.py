from dataclasses import dataclass


@dataclass
class Connessione:
    l1: str
    l2: str
    g1: str
    g2: str
    t: int
    peso: int
