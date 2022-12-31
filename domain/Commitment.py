from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


@dataclass_json
@dataclass
class Commitment:
    A: int = field(metadata=config(encoder=str, decoder=int))
    B: int = field(metadata=config(encoder=str, decoder=int))

