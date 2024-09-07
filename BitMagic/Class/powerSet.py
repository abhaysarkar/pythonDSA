

# def powerSet(str):
#     n = (1<<len(str))
#     print(n)

#     for i in range(0, n):
#         subset = ""
#         for j in range(0, len(str)):
#             if((i & (1<<j))):
#                 subset = subset + str[j]
#         print(subset)


def powerSet(s):
    n = 1 << len(s)  # Equivalent to 2^len(s)

    for i in range(1, n):  # Start from 1 to avoid the empty subset
        for j in range(len(s)):
            if i & (1 << j):  # Check if the jth bit is set in i
                print(s[j], end="")  # Print the character without newline
        print()  # Move to the next line after each subset

# Example usage
powerSet("abc")



str = 'abc'
powerSet(str)
