"""Prototype documentaire : distinguer préconfirmation et finalité Base."""

STATES=("observed","preconfirmed","safe","finalized")

def can_progress(previous,current):
    return previous in STATES and current in STATES and STATES.index(current)>=STATES.index(previous)

def release_allowed(state, policy="finalized"):
    return state in STATES and STATES.index(state)>=STATES.index(policy)

if __name__ == "__main__":
    assert can_progress("preconfirmed","safe")
    assert not can_progress("finalized","observed")
    assert release_allowed("finalized")
    assert not release_allowed("preconfirmed")
