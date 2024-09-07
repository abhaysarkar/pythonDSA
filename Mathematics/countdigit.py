import math

num = 12345
count = 0

print(math.ceil(math.log10(num)))

while num>0:
    num = num//10
    count = count + 1
print(count)
