num  = 17

def ispowoftwo(num):
    if num&(num-1) == 0:
        return True
    else:
        return False


print(ispowoftwo(num))