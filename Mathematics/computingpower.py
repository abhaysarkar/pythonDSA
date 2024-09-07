# import math
# num = 3
# exp = 4

# print(3**4)
# print(3**0.5)
# print(math.pow(3, 4))

def power(x, n):
    res = 1
    while n>0:
        if n%2 != 0:
            res = res * x
        x = x*x
        n = n//2
    return res

print(power(3,5))


