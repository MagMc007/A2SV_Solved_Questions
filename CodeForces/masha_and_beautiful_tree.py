# https://codeforces.com/problemset/problem/1741/D
# D. Masha and a Beautiful Tree
import sys

sys.setrecursionlimit(2000)

input_data = sys.stdin.read().split()
idx = 0

t = int(input_data[idx])
idx += 1

results = []

for _ in range(t):
    m = int(input_data[idx])
    idx += 1
    
    p = list(map(int, input_data[idx: idx + m]))
    idx += m
    
    cnt = 0
    possible = True

    def divide_and_conquer(l, r):
        global cnt, possible
        
        length = r - l
        
        if length == 1:
            return p[l]
        
        mid = (l + r) // 2
        
        left_min = divide_and_conquer(l, mid)
        right_min = divide_and_conquer(mid, r)
        
        if not possible:
            return -1
        
        half_size = length // 2
        
        if abs(left_min - right_min) != half_size:
            possible = False
            return -1
        
        if left_min > right_min:
            cnt += 1
            return right_min
        else:
            return left_min

    divide_and_conquer(0, m)

    if possible:
        results.append(str(cnt))
    else:
        results.append("-1")

sys.stdout.write("\n".join(results) + "\n")