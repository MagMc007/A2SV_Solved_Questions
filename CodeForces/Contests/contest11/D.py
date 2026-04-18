def get_mex(arr, n):
    # gets MEX each time
    seen = [False] * (n + 1)
    for x in arr:
        if x <= n:
            seen[x] = True
    for i in range(n + 1):
        if not seen[i]:
            return i
    return n


t = int(input())
for _ in range(t):
    n = int(input())

    # Read the array
    a = list(map(int, input().split()))

    ans = []

    while True:
        # Check if the array is already non-decreasing
        is_sorted = True

        for i in range(n - 1):
            if a[i] > a[i+1]:
                is_sorted = False
                break

        if is_sorted:  # array sorted (break out)
            break
            
        mex = get_mex(a, n)  # guaranteed to be less than or = n

        # goal is placing all elements at their index
        if mex < n:
            # place MEX at its index
            a[mex] = mex
            ans.append(mex + 1)  # as it is 1 based
        else:
            # MEX is n, find the first misplaced element and replace it
            for i in range(n):
                if a[i] != i:
                    a[i] = mex
                    ans.append(i + 1)  # Store 1-based index
                    break
                    
    # Output the number of moves and the moves themselves
    print(len(ans))
    print(*(ans))
