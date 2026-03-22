def can_make(n, m):
    if n == m:
        return True
    
    if n < m or n % 3 != 0:
        return False
    
    return can_make(n // 3, m) or can_make(2 * n // 3, m)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print("YES" if can_make(n, m) else "NO")