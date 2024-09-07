import math
a = 12
b = 8

print(math.gcd(12, 8))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
print(gcd(a, b))