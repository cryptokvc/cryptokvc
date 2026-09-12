"""Prototype pédagogique : liaison d'un proof aux entrées publiques."""

def public_input_digest(inputs):
    return hash(tuple(sorted(inputs.items()))) if isinstance(inputs,dict) else None

def proof_targets_inputs(proof, inputs):
    return isinstance(proof,dict) and proof.get("public_digest")==public_input_digest(inputs)

if __name__ == "__main__":
    i={"amount":7,"asset":"A"}
    p={"public_digest":public_input_digest(i)}
    assert proof_targets_inputs(p,i)
    assert not proof_targets_inputs(p,{"amount":8,"asset":"A"})
