from dataclasses import dataclass
from typing import List
from Voter import Voter


@dataclass
class VoterList:
    voters: List[Voter]
