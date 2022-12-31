import datetime
from dataclasses import dataclass
from Vote import Vote


@dataclass
class CastVote:
    cast_at: datetime
    vote: Vote
    vote_hash: str
    voter_hash: str
    voter_uuid: str

