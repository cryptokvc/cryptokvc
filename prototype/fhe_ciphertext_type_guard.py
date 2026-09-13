"""Policy checks for versioned FHE ciphertext operations."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Ciphertext:
    key_version: int
    kind: str
    context: str

def authorize(cipher: Ciphertext, expected_key: int, expected_kind: str, expected_context: str, operation: str) -> str:
    if cipher.key_version != expected_key: return "deny:key-version"
    if cipher.kind != expected_kind: return "deny:type"
    if cipher.context != expected_context: return "deny:context"
    if operation not in {"add", "multiply", "compare", "decrypt"}: return "deny:operation"
    return "allow"

if __name__ == "__main__":
    print(authorize(Ciphertext(2, "u32", "app"), 2, "u32", "app", "add"))
