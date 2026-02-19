# https://codeforces.com/problemset/problem/1165/B
# B. Polycarp Training
n = int(input())
cons = list(map(int, input().split()))
cons.sort()

days = 0
increament = 1

for i in cons:
    if i >= increament:
        days += 1
        increament += 1

print(days)
