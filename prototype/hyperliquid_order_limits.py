"""Prototype documentaire : bornes de risque d'un ordre Hyperliquid."""

def order_within_limits(order, max_notional, max_leverage):
    required=("price","size","leverage")
    if not isinstance(order,dict) or any(order.get(k) is None for k in required): return False
    p,s,l=order["price"],order["size"],order["leverage"]
    return all(isinstance(x,(int,float)) for x in (p,s,l)) and p>0 and s>0 and 0<l<=max_leverage and p*s<=max_notional

if __name__ == "__main__":
    assert order_within_limits({"price":10,"size":2,"leverage":3},100,5)
    assert not order_within_limits({"price":60,"size":2,"leverage":3},100,5)
