# https://codeforces.com/gym/673679/problem/A
n = int(input())
games = list(map(int, input().split()))

max_ = max(games)
sum_ = sum(games)

played = max_ * ((max_ + 1) / 2)
missing = int(played) - sum_

if missing == 0:
    print(max_ + 1)
else:
    print(missing)

