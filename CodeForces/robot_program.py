# https://codeforces.com/problemset/problem/2070/B
# B. Robot Program
t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()

    # build prefix movement
    pref = []
    cur = 0
    for ch in s:
        if ch == 'L':
            cur -= 1
        else:
            cur += 1
        pref.append(cur)

    # first time reaching 0 from start x 
    first_hit = -1
    for i in range(n):
        if x + pref[i] == 0:
            first_hit = i + 1
            break

    # if never hits 0 or hits after k seconds
    if first_hit == -1 or first_hit > k:
        print(0)
        continue

    # we got first hit
    ans = 1
    remaining = k - first_hit

    #  cycle length starting from 0
    cycle = -1
    for i in range(n):
        if pref[i] == 0:
            cycle = i + 1
            break

    # if no cycle → no more hits
    if cycle == -1:
        print(ans)
    else:
        ans += remaining // cycle
        print(ans)