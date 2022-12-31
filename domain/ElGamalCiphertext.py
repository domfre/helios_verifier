from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


@dataclass_json
@dataclass
class ElGamalCiphertext:
    alpha: int = field(metadata=config(encoder=str, decoder=int))
    beta: int = field(metadata=config(encoder=str, decoder=int))

    