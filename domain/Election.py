import datetime
from .ElGamalPublicKey import ElGamalPublicKey
from .QuestionList import QuestionList
from dataclasses import dataclass


@dataclass
class Election:
    cast_url: str
    description: str
    frozen_at: datetime
    name: str
    public_key: ElGamalPublicKey
    openreg: bool
    questions: QuestionList
    short_name: str
    use_voter_aliases: bool
    uuid: str
    voters_hash: str


