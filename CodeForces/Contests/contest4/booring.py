t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    cards = list(map(int, input().split()))

    left = 0

    wins = 0
    window_sum = 0

    for right in range(n):
        window_sum += cards[right]
        
        while window_sum > r:
            window_sum -= cards[left]
            left += 1
        
        if l <= window_sum <= r:
            wins += 1
            left = right + 1
            window_sum = 0
        
    print(wins)

