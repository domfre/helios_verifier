from dataclasses import dataclass
from typing import List
from ZkProof import ZkProof


@dataclass
class ZkProofZeroMax:
    zk_proofs: List[ZkProof]
