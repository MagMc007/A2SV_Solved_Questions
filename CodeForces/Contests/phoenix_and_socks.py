# https://codeforces.com/problemset/problem/1515/D
# D. Phoenix and Socks
t = int(input())
ans = []

for _ in range(t):
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    
    for i in range(l):
        left[arr[i]] += 1
    
    for i in range(l, n):
        right[arr[i]] += 1
    
    for i in range(1, n + 1):
        m = min(left[i], right[i])
        left[i] -= m
        right[i] -= m
    
    sl = sum(left)
    sr = sum(right)
    
    if sr > sl:
        left, right = right, left
        sl, sr = sr, sl
    
    diff = sl - sr
    move = diff // 2
    
    pairs = 0
    for i in range(1, n + 1):
        pairs += left[i] // 2
    
    use = min(pairs, move)
    
    cost = move + (sl + sr - 2 * use) // 2
    print(cost)
