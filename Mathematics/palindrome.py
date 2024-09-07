num = 123321

rev = str(num)
if(num == int(rev[::-1])):
    print("Given number is palindrome")
else:
    print("Given number is not palindrom")

temp = num
rev = 0
while temp>0:
    rev = rev*10 + temp%10
    temp = temp//10
if(num == rev):
    print("Given number is palindrome")
else:
    print("Given number is not palindrom")