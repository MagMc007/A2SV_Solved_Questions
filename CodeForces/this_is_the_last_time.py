# https://codeforces.com/problemset/problem/2126/D
# D. This Is the Last Time
t = int(input())

for _ in range(t):
    # n - casinos k- coins u have
    n, k = map(int, input().split())
    casinos = []

    for _ in range(n):
        casino = list(map(int, input().split()))
        casinos.append(casino)
    
    sorted_3 = sorted(casinos, key=lambda x: x[2])
    
