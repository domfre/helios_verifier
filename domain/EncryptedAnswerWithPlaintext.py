from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

from helios_verifier.domain.ElGamalCiphertext import ElGamalCiphertext
from helios_verifier.domain.ZkProof import ZkProof


@dataclass_json
@dataclass
class EncryptedAnswerWithPlaintext:
    answer: int
    choices: List[ElGamalCiphertext]
    individual_proofs: List[List[ZkProof]]
    overall_proof: List[ZkProof]
    randomness: List[int]

    def __post_init__(self):
        if self.randomness is not None:
            self.randomness = [int(r) for r in self.randomness]
