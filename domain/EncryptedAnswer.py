from dataclasses import dataclass
from typing import List
from.ElGamalCiphertext import ElGamalCiphertext


@dataclass
class EncryptedAnswer:
    choices: List[ElGamalCiphertext]
    individual_proofs: List[str]
    overall_proof: str
