from dataclasses import dataclass


@dataclass
class Voter:
    name: str
    uuid: str
    voter_id: str
    voter_type: str

