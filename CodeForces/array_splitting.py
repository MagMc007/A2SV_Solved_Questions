# https://codeforces.com/problemset/problem/1197/C
# C. Array Splitting
from collections import Counter
n, k = map(int, input().split())
arr = list(map(int, input().split()))

counter = Counter(arr)
# arr is sorted
# k divisions 
subArr = []

