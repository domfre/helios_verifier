import datetime
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from helios_verifier.domain.Vote import Vote


@dataclass_json
@dataclass
class CastVote:
    cast_at: datetime
    vote: Vote
    vote_hash: str
    voter_hash: str
    voter_uuid: str

    def __post_init__(self):
        if self.cast_at is None:
            return
        self.cast_at = datetime.datetime.strptime(self.cast_at.split('.')[0], '%Y-%m-%d %H:%M:%S')
