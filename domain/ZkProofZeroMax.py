from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

from helios_verifier.domain.ZkProof import ZkProof


@dataclass_json
@dataclass
class ZkProofZeroMax:
    zk_proofs: List[ZkProof]
