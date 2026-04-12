# https://codeforces.com/problemset/problem/616/D
# D. Longest k-Good Segment
n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = {}
distinct = 0

l = 0
best_l = 0
best_r = 0
max_len = 0

for r in range(n):
    if a[r] not in cnt or cnt[a[r]] == 0:
        distinct += 1
        cnt[a[r]] = 0
    cnt[a[r]] += 1

    while distinct > k:
        cnt[a[l]] -= 1
        if cnt[a[l]] == 0:
            distinct -= 1
        l += 1

    if r - l + 1 > max_len:
        max_len = r - l + 1
        best_l = l
        best_r = r

print(best_l + 1, best_r + 1)