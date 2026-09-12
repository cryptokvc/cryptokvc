"""Prototype pédagogique : borne de profondeur d'une preuve récursive."""

def recursion_is_bounded(proof, max_depth):
    return (isinstance(proof,dict) and isinstance(proof.get("depth"),int)
            and isinstance(max_depth,int) and 0 <= proof["depth"] <= max_depth
            and proof.get("inner_digest") is not None)

def compose(outer, inner, max_depth):
    if not recursion_is_bounded(inner,max_depth): return None
    candidate={"depth":inner["depth"]+1,"inner_digest":outer.get("digest")}
    return candidate if recursion_is_bounded(candidate,max_depth) else None

if __name__ == "__main__":
    assert compose({"digest":"d"},{"depth":1,"inner_digest":"x"},2)["depth"]==2
    assert compose({"digest":"d"},{"depth":2,"inner_digest":"x"},2) is None
