from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

from helios_verifier.domain.EncryptedAnswerWithPlaintext import EncryptedAnswerWithPlaintext


@dataclass_json
@dataclass
class VoteWithPlaintext:
    answers: List[EncryptedAnswerWithPlaintext]
    election_hash: str
    election_uuid: str
