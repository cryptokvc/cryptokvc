"""Prototype documentaire : borne de gaz avant soumission EVM."""

def gas_is_bounded(estimate, limit, margin):
    return (all(isinstance(x,int) for x in (estimate,limit,margin))
            and estimate >= 0 and margin >= 0 and limit >= estimate + margin)

def submit_allowed(estimate, limit, margin, balance, max_fee):
    return gas_is_bounded(estimate,limit,margin) and balance >= limit*max_fee

if __name__ == "__main__":
    assert submit_allowed(21000,30000,5000,3000000,1)
    assert not submit_allowed(21000,25000,5000,3000000,1)
