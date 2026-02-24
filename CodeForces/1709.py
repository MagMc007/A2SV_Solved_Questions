# https://codeforces.com/problemset/problem/2121/D
# D. 1709

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i = 0
    # operations
    k = 0
    opn = []

    # bubble sort sort both
    for i in range(n):
        for j in range(n-i-1):
            if k > 1709:
                break

            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                k += 1
                opn.append([1, j+1]) 
            
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                k += 1
                opn.append([2, j+1]) 

    # cross check
    if k <= 1709:
        for i in range(n):
            if a[i] > b[i]:
                a[i], b[i] = b[i], a[i]
                opn.append([3, i+1])
                k += 1
    
    print(k)
    for op in opn:
        print(*op)
