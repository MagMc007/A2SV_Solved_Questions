# https://codeforces.com/problemset/problem/2065/C2
# C2. Skibidus and Fanum Tax (hard version)
from bisect import bisect_left

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()

    # minimize at each step greedily
    prev = min(a[0], b[0] - a[0])

    status = True

    for i in range(1, n):
        idx = bisect_left(b, a[i] + prev)

        # no element and no order
        if idx == m and a[i] < prev: 
            status = False
            break
        
        # no element but satiesfies order
        if idx == m:
            prev = a[i]
            continue

        # can be transformed
        trans = b[idx] - a[i]

        if a[i] >= prev:
            prev = min(a[i], trans)
        else:
            prev = trans

    if status:
        print("YES")
    else:
        print("NO")
