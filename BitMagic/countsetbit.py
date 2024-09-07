num = 15

#Integer to binary String
ans = bin(num)  
# print(ans)  #output = 0b1100

# print(ans.count('b'))
# print(ans.count('1'))
# print(ans.count('0'))

ans = format(num, 'b') # 'b' for binary , 'o' for octal, 'x' for hexadecimal

print(ans)  #output = 1100
# print(ans.count('b'))
# print(ans.count('1'))
# print(ans.count('0'))

def countsetbit(num):
    count = 0
    while num:
        count = count + 1
        num = num & (num-1)
    return count

num = 15
# print(countsetbit(num))