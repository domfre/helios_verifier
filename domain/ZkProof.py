from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config

from helios_verifier.domain.Commitment import Commitment


@dataclass_json
@dataclass
class ZkProof:
    challenge: int = field(metadata=config(encoder=str, decoder=int))
    commitment: Commitment
    response: int = field(metadata=config(encoder=str, decoder=int))

    