# https://codeforces.com/gym/675123/problem/A
t = int(input())

for _ in range(t):
    palin = input()

    uniques = set(palin)
    # print(uniques)

    if len(uniques) > 2:
        print("YES")
    elif len(uniques) == 2 and len(palin) % 2 == 0:
        # how about ababababa
        # uniques are 2 and length is 9, 9 % 2 = 1
        # it is a NO, but not
        print("YES")
    else:
        print("NO")


# t = int(input())

# for _ in range(t):
#     s = input()
#     n = len(s)
    
#     first_half = s[:n // 2]
    
#     if len(set(first_half)) > 1:
#         print("YES")
#     else:
#         print("NO")

"""
    My mistake:
      **i did not have enough edge cases to change things around
        my approach did not consider things like ababa**

        my other problem was i did not change my approach(i submitted
        the same answer twice, that is dumb
        switch up
    )
"""