"""Small model for reviewing expected EVM storage accesses."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Access:
    address: str
    slot: str
    mode: str

def unexpected(actual: list[Access], expected: set[tuple[str,str]]) -> list[Access]:
    return [item for item in actual if (item.address, item.slot) not in expected]

def invalid_modes(accesses: list[Access]) -> list[Access]:
    return [item for item in accesses if item.mode not in {"read", "write"}]

if __name__ == "__main__":
    trace=[Access("0xabc", "0x01", "read")]
    print(unexpected(trace, {("0xabc", "0x01")}))
