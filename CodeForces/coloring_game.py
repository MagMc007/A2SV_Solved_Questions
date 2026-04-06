# https://codeforces.com/problemset/problem/2112/C
# C. Coloring Game
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    # arr is provide in sorted order

    ans = 0
    max_ = arr[-1]

    # to win
    # 1. bob recolors Alice's largest, so alice needs: a[i] + a[j] > a[k]
    # 2. bob colors the largest uncolored (max_), Alice needs: a[i] + a[j] + a[k] > max_
    # so a[i] + a[j] > max_- a[k]

    for k in range(2, n):
        need = max(arr[k], max_ - arr[k])

        i = 0 # smalles available
        j = k - 1  # largest in the current range

        while i < j:
            # go back and look for all combinations
            if arr[i] + arr[j] > need:
                ans += j - i

                j -= 1
            else:
                i += 1

    print(ans)




