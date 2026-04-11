# https://codeforces.com/gym/684794/problem/A
t = int(input())

for _ in range(t):
    n, h = map(int, input().split())
    ans = 0

    for _ in range(n):
        w, l = map(int,  input().split())
        ans += max(w, l)
    
    if ans >= h:
        print("YES")
    else:
        print("NO")