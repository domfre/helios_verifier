from dataclasses import dataclass
from typing import List
from .EncryptedAnswerWithPlaintext import EncryptedAnswerWithPlaintext


@dataclass
class VoteWithPlaintext:
    answers: List[EncryptedAnswerWithPlaintext]
    election_hash: str
    election_uuid: str