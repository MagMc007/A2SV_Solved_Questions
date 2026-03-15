from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    flag = True
    cnt = Counter(s)

    idx = []

    for k, v in cnt.items():
        if v == 1:
            flag = False
            break
        idx.append(v + len(idx))
        l = len(idx)

        app = [l + i for i in range(v-1)]
        idx.extend(app)

    if not flag:
        print(-1)
    else:
        print(*idx)