import datetime

from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import List

from helios_verifier.domain.ElGamalPublicKey import ElGamalPublicKey
from helios_verifier.domain.Question import Question


@dataclass_json
@dataclass
class Election:
    cast_url: str
    description: str
    frozen_at: datetime
    name: str
    openreg: bool
    public_key: ElGamalPublicKey
    questions: List[Question]
    short_name: str
    use_voter_aliases: bool
    uuid: str
    voters_hash: str


