from collections import Counter

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    degree = Counter()
    for _ in range(m):
        u, v = map(int, input().split())
        degree[u] += 1
        degree[v] += 1
    
    non_leafs = []
    for node in degree:
        if degree[node] > 1:
            non_leafs.append(degree[node])
    
    counts = {}
    for d in non_leafs:
        if d not in counts:
            counts[d] = 0
        counts[d] += 1

    x = None
    y = None

    # print(counts)
    if len(non_leafs) == 1:
        x = list(counts.keys())[0]
        y = x - 1
    else:
        for deg in counts:
            freq = counts[deg]
            if freq == 1:
                x = deg
            else:
                y = deg - 1
    print(x, y)