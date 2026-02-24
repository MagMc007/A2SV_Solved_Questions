# https://codeforces.com/problemset/problem/1251/A
#  A. Broken Keyboard

t = int(input())

for _ in range(t):
    typed = input()

    res = set()

    i = 0
    j = i + 1
    cnt = 1

    while j < len(typed):
        if typed[i] == typed[j]:
            j += 1
            cnt += 1
        else:
            if cnt % 2 != 0:
                res.add(typed[i])
            i = j
            j += 1
            cnt = 1
    
    # the last element
    if cnt % 2 != 0:
        res.add(typed[i])
    res = list(res)
    res.sort()
    print("".join(res))
