from dataclasses import dataclass


@dataclass
class ZkProof:
    challenge: int
    commitment: dict
    response: int
    