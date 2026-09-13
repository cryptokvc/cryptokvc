"""Defensive checks before consuming a Hyperliquid reference price."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Price:
    value: str
    timestamp: int
    decimals: int

def accept(price: Price, now: int, max_age: int, tolerance: str) -> str:
    if price.decimals < 0 or not price.value: return "deny:format"
    if now < price.timestamp or now-price.timestamp > max_age: return "deny:stale"
    if tolerance == "": return "deny:missing-tolerance"
    return "allow"

if __name__ == "__main__":
    print(accept(Price("2000", 90, 2), 100, 30, "0.01"))
