import math
num = 5

print(math.factorial(num))

fact = 1
for i in range(1, num+1):
    fact = fact*i
    print(i)

print(f'Factorial of a number is {fact}')
