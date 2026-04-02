t = int(input())

for _ in range(t):
    D, T = map(int, input().split())

    left = 1
    right = D

    ans = 0

    while right >= T:
        middle = (left + right) // 2
        ans += 1

        if middle <= T:
            break
        
        if middle > T:
            right = middle
    
    print(ans)