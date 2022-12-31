from dataclasses import dataclass
from typing import List
from ElGamalCiphertext import ElGamalCiphertext


@dataclass
class EncryptedAnswerWithPlaintext:
    answer: int
    choices: List[ElGamalCiphertext]
    individual_proofs: List[str]
    overall_proof: str
    randomness: List[int]
