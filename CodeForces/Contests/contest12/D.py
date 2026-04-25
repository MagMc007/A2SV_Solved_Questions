# # =================================
import sys

def solve():
    # Fast I/O
    input = sys.stdin.read().split()
    if not input: return
    
    n = int(input[0])
    ax, ay = int(input[1]), int(input[2]) # Queen
    bx, by = int(input[3]), int(input[4]) # King start
    cx, cy = int(input[5]), int(input[6]) # Target

    # 1. Use a 2D array instead of a set for much faster lookups
    # visited[row][col]
    visited = [[False] * (n + 1) for _ in range(n + 1)]

    # 2. Iterative DFS using a manual stack
    stack = [(bx, by)]
    visited[bx][by] = True

    dxns = [(-1, 0), (1, 0), (0, 1), (0, -1),
            (-1, -1), (1, 1), (-1, 1), (1, -1)]

    while stack:
        r, c = stack.pop()

        # Check if we reached the target
        if r == cx and c == cy:
            print("YES")
            return

        for dr, dc in dxns:
            nr, nc = r + dr, c + dc

            # Check bounds
            if 1 <= nr <= n and 1 <= nc <= n:
                # Check if already visited
                if not visited[nr][nc]:
                    # Check Queen safety (Row, Column, and both Diagonals)
                    if nr != ax and nc != ay and (ax - ay) != (nr - nc) and (ax + ay) != (nr + nc):
                        visited[nr][nc] = True
                        stack.append((nr, nc))

    print("NO")

solve()