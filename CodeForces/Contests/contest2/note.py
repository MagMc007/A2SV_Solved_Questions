# https://codeforces.com/gym/671638/problem/C
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    words = {}
    word = ""
    flag = False
    i = 0

    while i < len(s) - 1:
        snippet = s[i] + s[i + 1]
        if snippet in words:
            if words[snippet] != i:
                flag = True
                break
        else:
            words[snippet] = i + 1
        i += 1

    if flag:
        print("YES")
    else:
        print("NO")
