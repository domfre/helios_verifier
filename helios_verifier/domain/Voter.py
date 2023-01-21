from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Voter:
    election_uuid: str
    name: str
    uuid: str
    voter_id_hash: str
    voter_type: str

