# https://codeforces.com/problemset/problem/2056/B
# B. Find the Permutation
from collections import defaultdict
t = int(input())

for _ in range(t):
    ans = []
    graph = defaultdict(list)
