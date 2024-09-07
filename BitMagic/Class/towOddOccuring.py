def twoOddOccuring(arr):
    num  = arr[0]
    for i in range(1, len(arr)):
        num = num^arr[i]
    num = num & ~(num-1)
    res1 = 0
    res2 = 0
    for i in range(0, len(arr)):
        if(arr[i]&num):
            res1 = res1^arr[i]
        else:
            res2 = res2^arr[i]
    return [res1, res2]

arr = [3, 4, 3, 4, 5, 4, 4, 6, 7, 7]

print(twoOddOccuring(arr))

