from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

from helios_verifier.domain.EncryptedAnswer import EncryptedAnswer


@dataclass_json
@dataclass
class Vote:
    answers: List[EncryptedAnswer]
    election_hash: str
    election_uuid: str
