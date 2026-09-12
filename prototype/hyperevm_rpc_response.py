"""Prototype documentaire : validation défensive d'une réponse RPC HyperEVM."""

def rpc_result_is_valid(response, request_id):
    return (isinstance(response,dict) and response.get("id")==request_id
            and response.get("jsonrpc")=="2.0" and response.get("error") is None
            and response.get("result") is not None)

def accept_block_response(response,request_id,expected_hash):
    return rpc_result_is_valid(response,request_id) and response["result"].get("hash")==expected_hash

if __name__ == "__main__":
    r={"jsonrpc":"2.0","id":1,"result":{"hash":"h"}}
    assert accept_block_response(r,1,"h")
    assert not accept_block_response({**r,"id":2},1,"h")
