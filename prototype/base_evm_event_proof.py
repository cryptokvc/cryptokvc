"""Prototype documentaire : rapprochement d'un reçu EVM et d'un événement."""

def event_matches(receipt,event):
    keys=("tx_hash","block_number","contract","topic0","data_hash")
    return (all(receipt.get(k) is not None for k in keys) and all(event.get(k) is not None for k in keys)
            and all(receipt[k]==event[k] for k in keys))

def finalized_event(receipt,event,finalized_block):
    return event_matches(receipt,event) and receipt["block_number"] <= finalized_block

if __name__ == "__main__":
    r={"tx_hash":"t","block_number":10,"contract":"c","topic0":"x","data_hash":"d"}
    assert finalized_event(r,dict(r),12)
    assert not finalized_event(r,dict(r),9)
