def kthbitsetornot(num, k):
    flag = 1<<(k-1)
    if flag&num != 0:
        return True
    else:
        return False

print(kthbitsetornot(8, 3))