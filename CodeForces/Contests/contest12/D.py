import sys

def solve():
    line1 = sys.stdin.readline().split()
    if not line1: return
    n, m = map(int, line1)
    
    degree = [0] * (n + 1)
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        degree[u] += 1
        degree[v] += 1

    # Frequency map: how many nodes have a specific degree
    # count_map[degree] = number_of_nodes_with_this_degree
    count_map = {}
    for i in range(1, n + 1):
        d = degree[i]
        count_map[d] = count_map.get(d, 0) + 1
    
    remaining_degrees = []
    for d, freq in count_map.items():
        if d != 1:
            remaining_degrees.append((d, freq))
            
    if len(remaining_degrees) == 2:
        for d, freq in remaining_degrees:
            if freq == 1:
                x = d
            else:
                y = d - 1
    else:
        d, freq = remaining_degrees[0]
        x = freq - 1
        y = d - 1
        
    print(x, y)


t_str = sys.stdin.readline().strip()
if t_str:
    t = int(t_str)
    for _ in range(t):
        solve()