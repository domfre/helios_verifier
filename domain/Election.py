import datetime

from dataclasses_json import dataclass_json, config
from dataclasses import dataclass, field
from typing import List

from helios_verifier.domain.ElGamalPublicKey import ElGamalPublicKey
from helios_verifier.domain.Question import Question


@dataclass_json
@dataclass
class Election:
    cast_url: str
    description: str
    name: str
    openreg: bool
    public_key: ElGamalPublicKey
    questions: List[Question]
    short_name: str
    use_voter_aliases: bool
    uuid: str
    voters_hash: str
    frozen_at: datetime

    def __post_init__(self):
        self.frozen_at = datetime.datetime.strptime(self.frozen_at.split('.')[0], '%Y-%m-%d %H:%M:%S')

