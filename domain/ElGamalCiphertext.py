from dataclasses import dataclass


@dataclass
class ElGamalCiphertext:
    alpha: str
    beta: str

    