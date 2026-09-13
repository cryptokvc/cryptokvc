"""Classify disagreements between HyperEVM RPC observations."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Observation:
    endpoint: str
    block: int
    block_hash: str
    state_root: str

def quorum(observations: list[Observation]) -> dict[str, object]:
    if not observations: return {"status":"empty"}
    blocks={x.block for x in observations}; hashes={x.block_hash for x in observations}; roots={x.state_root for x in observations}
    return {"status":"agree" if len(blocks)==len(hashes)==len(roots)==1 else "divergent", "blocks":sorted(blocks), "hashes":len(hashes), "roots":len(roots)}

if __name__ == "__main__":
    print(quorum([Observation("a", 1, "h", "r"), Observation("b", 1, "h", "r")]))
