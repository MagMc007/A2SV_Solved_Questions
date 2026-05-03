# https://codeforces.com/contest/510/problem/C
# C. Fox And Names
from collections import deque

n = int(input())

visited = set()
graph = [[] for _ in range(26)]
in_degree = [0] * 26

# construct the graph
names = []
for _ in range(n):
    name = input()
    names.append(name)

possible = True
# Build the graph by comparing adjacent words
for i in range(n - 1):
    w1 = names[i]
    w2 = names[i+1]
    
    min_len = min(len(w1), len(w2))
    found_diff = False
    
    for j in range(min_len):
        if w1[j] != w2[j]:
            # use ascii as index
            u = ord(w1[j]) - ord('a')
            v = ord(w2[j]) - ord('a')
            # u >> v
            graph[u].append(v)
            in_degree[v] += 1
            found_diff = True
            break
    
    if not found_diff and len(w1) > len(w2):
        print("Impossible")
        possible = False
        break

if possible:
    q = deque()

    for i in range(26):
        if in_degree[i] == 0:
            q.append(i)

    result = []
    # BFS-based topological sort
    idx = 0
    while q:
        u = q.popleft()
        idx += 1
        result.append(chr(u + ord('a')))
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    if len(result) < 26:
        print("Impossible")
    else:
        print("".join(result))