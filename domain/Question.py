from dataclasses import dataclass
from typing import List


@dataclass
class Question:
    answer_urls: List[str]
    answers: List[str]
    choice_type: str
    max: int
    min: int
    result_type: str
    question: str
    short_name: str
    tally_type: str
