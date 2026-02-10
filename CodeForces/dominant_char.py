# https://codeforces.com/problemset/problem/1605/C
# C. Dominant Character

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    if "aa" in s:
        print(2)
    else:
        if 'aca' in s or 'aba' in s:
            print(3)
        else:
            if 'abca' in s or 'acba' in s:
                print(4)
            elif 'abbacca' in s or 'accabba' in s:
                print(7)
            else:
                print(-1)