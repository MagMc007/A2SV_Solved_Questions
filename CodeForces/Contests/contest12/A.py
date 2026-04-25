# https://codeforces.com/gym/688931/problem/A
t = int(input())

for _ in range(t):
    cnt = 0

    pi = "314159265358979323846264338327"
    inp = input()

    i = 0

    while i < len(inp):
        if pi[i] == inp[i]:
            cnt += 1
        else:
            break
        i += 1
    print(cnt)