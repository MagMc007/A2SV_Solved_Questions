# https://codeforces.com/contest/710/problem/B
# B. Optimal Point on a Line
n = int(input())
x = list(map(int, input().split()))

# x may not be in a sorted order
x.sort()
if n % 2 != 0:
    print(x[n//2])
else:
    print(x[n//2 - 1])

