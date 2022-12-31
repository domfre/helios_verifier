from dataclasses import dataclass
from typing import List
from EncryptedAnswer import EncryptedAnswer


@dataclass
class Vote:
    answers: List[EncryptedAnswer]
    election_hash: str
    election_uuid: str
