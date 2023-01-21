import datetime
from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from helios_verifier.domain.Vote import Vote


@dataclass_json
@dataclass
class CastVote:
    cast_at: datetime
    vote: Vote
    vote_hash: Optional[str]
    voter_hash: Optional[str]
    voter_uuid: str

    def __post_init__(self):
        if self.cast_at is not None:
            self.cast_at = datetime.datetime.strptime(self.cast_at.split('.')[0], '%Y-%m-%d %H:%M:%S')
