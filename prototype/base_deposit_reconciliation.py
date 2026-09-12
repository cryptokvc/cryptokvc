"""Prototype documentaire : réconciliation d'un dépôt L1/L2."""

def deposit_matches(l1, l2):
    keys=("tx_hash","amount","recipient","nonce")
    return (all(l1.get(k) is not None for k in keys) and all(l2.get(k) is not None for k in keys)
            and all(l1[k]==l2[k] for k in keys))

def accept_deposit(l1,l2,finalized):
    return finalized and deposit_matches(l1,l2)

if __name__ == "__main__":
    a={"tx_hash":"h","amount":5,"recipient":"u","nonce":2}
    assert accept_deposit(a,dict(a),True)
    assert not accept_deposit(a,dict(a),False)
    assert not accept_deposit(a,{**a,"amount":6},True)
