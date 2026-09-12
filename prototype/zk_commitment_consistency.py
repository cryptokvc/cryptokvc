"""Prototype pédagogique : cohérence d'un engagement et de son ouverture."""

def commit(value, salt):
    return hash((value,salt))

def opening_is_valid(commitment, value, salt):
    return commitment==commit(value,salt)

if __name__ == "__main__":
    c=commit("secret","salt")
    assert opening_is_valid(c,"secret","salt")
    assert not opening_is_valid(c,"other","salt")
