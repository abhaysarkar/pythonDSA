
def findOneOddOccuring(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        res = res^arr[i]
    return res



arr = [1, 2, 3, 4, 1, 5, 1, 2, 4, 1, 3]
print(findOneOddOccuring(arr))    
