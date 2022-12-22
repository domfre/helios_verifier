from dataclasses import dataclass
from typing import List
from.Question import Question


@dataclass
class QuestionList:
    questions: List[Question]
