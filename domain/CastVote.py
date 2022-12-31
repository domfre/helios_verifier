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
