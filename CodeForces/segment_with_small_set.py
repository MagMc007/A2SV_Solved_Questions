# https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/E
# E. Segments with Small Set
from collections import Counter

n, k = map(int, input().split())
arr = list(map(int, input().split()))

hash = Counter()

left = 0

cnt = 0

for right in range(n):
    hash[arr[right]] += 1

    while len(hash) > k:
        hash[arr[left]] -= 1
        if hash[arr[left]] == 0:
            hash.pop(arr[left])
        left += 1
    
    cnt += right - left + 1

print(cnt)