import math

def reduce_fraction(f):
    n, d = f
    gcd = math.gcd(n, d)
    return (n // gcd, d // gcd)