# https://codeforces.com/problemset/problem/1690/D
# D. Black and White Stripe
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    block = input()

    # fixed sliding window of size k
    paint = 0
    for i in range(k):
        if block[i] == 'W':
            paint += 1

    min_ = paint  # record the minimum paint needed

    left = 0
    for right in range(k, n):
        # add from the right
        if block[right] == 'W':
            paint += 1
        
        # move the left
        if block[left] == 'W':
            paint -= 1
        left += 1

        min_ = min(min_, paint)

    print(min_)