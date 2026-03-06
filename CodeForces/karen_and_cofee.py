# https://codeforces.com/contest/816/problem/B
# B. Karen and Coffee
from collections import Counter
n, k, q = map(int, input().split())

recipe = []
for _ in range(n):
    recipe.append(list(map(int, input().split())))

for _ in range(q):
    l, r = map(int, input().split())
    hash = Counter()
    cnt = 0
    for temp in range(l, r + 1):
        for low, high in recipe:
            if low <= temp <= high:
                hash[temp] += 1

                if hash[temp] >= 2:
                    cnt += 1
    print(cnt)
