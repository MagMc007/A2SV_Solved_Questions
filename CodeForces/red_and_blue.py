# https://codeforces.com/contest/1469/problem/B
# B. Red and Blue
t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))

    m = int(input())
    b = list(map(int, input().split()))

    # it is greedy in the sense that to get the
    # max we have to get the max from both r and b
    max_r = 0
    prefr = 0

    for i in r:
        prefr += i

        max_r = max(prefr, max_r)

    max_b = 0
    prefb = 0

    for j in b:
        prefb += j
        max_b = max(prefb, max_b)
        
    print(max_r + max_b)