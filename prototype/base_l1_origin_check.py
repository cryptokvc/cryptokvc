"""Documentary checks for an L1-originated Base message."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Origin:
    chain_id: int
    domain: str
    block: int
    tx_hash: str

def validate(origin: Origin, expected_chain: int, expected_domain: str) -> list[str]:
    errors=[]
    if origin.chain_id != expected_chain: errors.append("unexpected chain")
    if origin.domain != expected_domain: errors.append("unexpected domain")
    if origin.block < 0: errors.append("invalid block")
    if len(origin.tx_hash) != 66 or not origin.tx_hash.startswith("0x"): errors.append("invalid tx hash")
    return errors

if __name__ == "__main__":
    print(validate(Origin(1, "base-l1", 10, "0x"+"a"*64), 1, "base-l1"))
