t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    cards = list(map(int, input().split()))

    left = 0

    wins = 0
    curr = 0

    for right in range(n):
        if l <= cards[right] <= r:
            wins += 1

            if l <= curr <= r:
                wins += 1
        
            curr = 0
            left = right
            continue

        curr += cards[right]

        while 
        

        

        
    print(wins)

