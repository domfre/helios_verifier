from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List


@dataclass_json
@dataclass
class Trustee:
    decryption_factors: List[str]
    decryption_proofs: List[str]
    pok: str
    public_key: int
    public_key_hash: int
    uuid: str
