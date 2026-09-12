"""Prototype documentaire : cohérence d'un lot d'événements Hyperliquid."""

def batch_is_contiguous(events):
    if not events: return False
    seq=[e.get("sequence") for e in events]
    return all(isinstance(x,int) for x in seq) and seq==list(range(seq[0],seq[0]+len(seq)))

def batch_for_account(events,account):
    return batch_is_contiguous(events) and all(e.get("account")==account for e in events)

if __name__ == "__main__":
    es=[{"sequence":4,"account":"a"},{"sequence":5,"account":"a"}]
    assert batch_for_account(es,"a")
    assert not batch_for_account([{**es[0]},{"sequence":7,"account":"a"}],"a")
