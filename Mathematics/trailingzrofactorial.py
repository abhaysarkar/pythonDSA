import math
num = 500
print(math.factorial(num))
res = 0
div = 5
while num>=div:
    res = res + num//div
    div = div*5
print(f'No of trailing zeros in factorial is {res}')