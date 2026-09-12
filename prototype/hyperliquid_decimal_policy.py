"""Prototype documentaire : quantification déterministe des ordres."""

from decimal import Decimal, ROUND_DOWN

def quantize(value, decimals):
    if decimals < 0 or not isinstance(decimals,int): raise ValueError("invalid decimals")
    return Decimal(str(value)).quantize(Decimal(1).scaleb(-decimals),rounding=ROUND_DOWN)

def order_valid(price,size,price_decimals,size_decimals):
    try:
        p=quantize(price,price_decimals); s=quantize(size,size_decimals)
        return p>0 and s>0 and p==Decimal(str(price)) and s==Decimal(str(size))
    except (ValueError,ArithmeticError):
        return False

if __name__ == "__main__":
    assert order_valid("10.12","2.50",2,2)
    assert not order_valid("10.129","2.50",2,2)
