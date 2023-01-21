from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


@dataclass_json
@dataclass
class ElGamalPublicKey:
    g: int = field(metadata=config(encoder=str, decoder=int))
    p: int = field(metadata=config(encoder=str, decoder=int))
    q: int = field(metadata=config(encoder=str, decoder=int))
    y: int = field(metadata=config(encoder=str, decoder=int))


