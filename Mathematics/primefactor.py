
def primeFactors(num):
    res = []
    
    # Check for number of 2s
    while num % 2 == 0:
        res.append(2)
        num //= 2
    
    # Check for number of 3s
    while num % 3 == 0:
        res.append(3)
        num //= 3
    
    i = 5
    while i * i <= num:
        while num % i == 0:
            res.append(i)
            num //= i
        while num % (i + 2) == 0:
            res.append(i + 2)
            num //= (i + 2)
        i += 6
    
    # This condition is to check if num is a prime number greater than 4
    if num > 3:
        res.append(num)
    
    return res

print(primeFactors(34))       