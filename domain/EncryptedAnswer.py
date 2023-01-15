from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

from helios_verifier.domain.ElGamalCiphertext import ElGamalCiphertext
from helios_verifier.domain.ZkProof import ZkProof


@dataclass_json
@dataclass
class EncryptedAnswer:
    choices: List[ElGamalCiphertext]
    individual_proofs: List[List[ZkProof]]
    overall_proof: List[ZkProof]
