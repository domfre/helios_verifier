from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

from helios_verifier.domain.ZkProof import ZkProof
from helios_verifier.domain.ElGamalPublicKey import ElGamalPublicKey


@dataclass_json
@dataclass
class Trustee:
    decryption_factors: List[List[int]]
    decryption_proofs: List[List[ZkProof]]
    pok: str
    public_key: ElGamalPublicKey
    public_key_hash: int
    uuid: str

    def __post_init__(self):
        if self.decryption_factors is not None:
            self.decryption_factors = [[int(f) for f in df] for df in self.decryption_factors]
