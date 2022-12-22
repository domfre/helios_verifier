from dataclasses import dataclass


@dataclass
class ElGamalPublicKey:
    g: int
    p: int
    q: int
    y: int
