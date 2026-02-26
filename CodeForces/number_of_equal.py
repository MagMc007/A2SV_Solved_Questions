# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/C
# C. Number of Equal
from collections import Counter

n, m = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_m = list(map(int, input().split()))

n_cnt = Counter(arr_n)
m_cnt = Counter(arr_m)

# pointers on 2 arrays
pairs = 0

visited = set()

i, j = 0, 0

while i < n and j < m:
    if arr_n[i] == arr_m[j]:
        if not arr_n[i] in visited:
            # add the multiplication of the existing
            # counts
            pairs += n_cnt[arr_n[i]] * m_cnt[arr_n[i]]
            visited.add(arr_n[i])  
        i += 1
        j += 1
    elif arr_n[i] > arr_m[j]:
        j += 1
    else:
        i += 1

print(pairs)

# time => O(n + m)
# space may be on the set and dictionary
# => O(n + m)