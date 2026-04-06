# https://codeforces.com/problemset/problem/476/B
# B. Dreamoon and WiFi
from math import comb
s1 = input()
s2 = input()

target = 0
for i in s1:
    if i == "+":
        target += 1
    else:
        target -= 1

current = 0
for i in s2:
    if i == "+":
        current += 1
    elif i == "-":
        current -= 1

diff = target - current
uk = s2.count("?")

a = (uk + diff)

if a % 2 != 0 or a < 0:
    print(0)
else:
    a = a // 2
    if a > uk:
        print(0)
    else:
        prob = comb(uk, int(a)) / (2 ** uk)
        print(prob)