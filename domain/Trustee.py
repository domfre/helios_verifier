from dataclasses import dataclass
from typing import List


@dataclass
class Trustee:
    decryption_factors: List[str]
    decryption_proofs: List[str]
    pok: str
    public_key: int
    public_key_hash: int
    uuid: str
