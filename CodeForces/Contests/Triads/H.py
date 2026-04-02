t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    cnt = 0
    ptr1 = 0
    ptr2 = n-1

    while ptr1 < ptr2 and ptr1 < n:
        if ptr1 + 1 < n and s[ptr1 + 1] == s[ptr2]:
            ptr1 += 1
            cnt += 1
        else:
            ptr1 += 1
            ptr2 -= 1
    
    if ptr2 == ptr1:
        cnt += 1
    
    print(cnt)


