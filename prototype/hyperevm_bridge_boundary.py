"""Prototype documentaire : frontière de confiance d'un message Core/EVM."""

REQUIRED=("message_id","source_chain","destination_chain","nonce","payload_hash")

def message_is_well_formed(message, expected_source, expected_destination):
    return (isinstance(message,dict) and all(message.get(k) is not None for k in REQUIRED)
            and message["source_chain"]==expected_source
            and message["destination_chain"]==expected_destination
            and isinstance(message["nonce"],int) and message["nonce"]>=0)

def accept_message(message,last_nonce,source,destination):
    return message_is_well_formed(message,source,destination) and message["nonce"]>last_nonce

if __name__ == "__main__":
    m={"message_id":"m1","source_chain":"core","destination_chain":"evm","nonce":4,"payload_hash":"p"}
    assert accept_message(m,3,"core","evm")
    assert not accept_message(m,4,"core","evm")
    assert not accept_message(m,3,"other","evm")
