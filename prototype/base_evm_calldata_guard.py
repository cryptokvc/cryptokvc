"""Prototype documentaire : validation minimale d'un appel EVM sur Base."""

def calldata_is_safe(call, expected_chain, allowed_targets, allowed_methods):
    required=("chain_id","to","method","data")
    return (isinstance(call,dict) and all(call.get(k) is not None for k in required)
            and call["chain_id"]==expected_chain and call["to"] in set(allowed_targets)
            and call["method"] in set(allowed_methods) and isinstance(call["data"],str)
            and call["data"].startswith("0x"))

if __name__ == "__main__":
    c={"chain_id":8453,"to":"0xrouter","method":"swap","data":"0x1234"}
    assert calldata_is_safe(c,8453,["0xrouter"],["swap"])
    assert not calldata_is_safe({**c,"chain_id":1},8453,["0xrouter"],["swap"])
    assert not calldata_is_safe({**c,"method":"upgrade"},8453,["0xrouter"],["swap"])
