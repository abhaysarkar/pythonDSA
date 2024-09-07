num = 24

def alldivisor(num):
    res = []
    i = 1
    while num>=i*i:
        if num%i == 0:
            res.append(i)
            res.append(num//i)
            i = i+1
    return res
print(alldivisor(24))
res = alldivisor(24)
print(res)
print(res.sort())
print(res)