from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

from helios_verifier.domain.ElGamalCiphertext import ElGamalCiphertext


@dataclass_json
@dataclass
class EncryptedAnswerWithPlaintext:
    answer: int
    choices: List[ElGamalCiphertext]
    individual_proofs: List[str]
    overall_proof: str
    randomness: List[int]
