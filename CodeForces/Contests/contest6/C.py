from collections import Counter

n = int(input())
pup = input()

cnt = Counter(pup)
vals = cnt.values()

# only one of them has to be 2
if sum(vals) == len(cnt) and n != 1:
    print("NO")
else:
    print("YES")
