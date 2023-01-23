from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import List, Optional

from helios_verifier.domain.ElGamalPublicKey import ElGamalPublicKey
from helios_verifier.domain.Question import Question


@dataclass_json
@dataclass
class Election:
    cast_url: str
    description: str
    frozen_at: str
    name: str
    openreg: bool
    public_key: ElGamalPublicKey
    questions: List[Question]
    short_name: str
    use_voter_aliases: bool
    uuid: str
    voters_hash: Optional[str]
    voting_ends_at: Optional[str]
    voting_starts_at: Optional[str]

    def __post_init__(self):
        self.frozen_at = str(self.frozen_at)
        self.voting_ends_at = str(self.voting_ends_at)
        self.voting_starts_at = str(self.voting_starts_at)
