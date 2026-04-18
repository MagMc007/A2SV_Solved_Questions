t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    ans = 0

    for i in range(1, n, 2):
        # odd will not touch the last
        # the difference
        # ............E......N
        diff = arr[i - 1] - arr[i]

        # how much to increase arr[i] with
        if k > diff:
            k -= diff
            diff = 0
        else:
            diff -= k
            k = 0
            
        ans += diff
            
    if n % 2 != 0:
        ans += arr[-1]
    
    print(ans)