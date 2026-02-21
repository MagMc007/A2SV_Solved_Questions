# https://codeforces.com/problemset/problem/1197/C
# C. Array Splitting
n, k = map(int, input().split())
arr = list(map(int, input().split()))

if k == 1:
    print(arr[-1] - arr[0])
else:
    diff = []

    for i in range(len(arr)-1):
        diff.append(arr[i+1] - arr[i])

    diff.sort(reverse=True)
    # print(diff)

    # if it was 1 grp
    total = arr[-1] - arr[0]

    # but there is k group
    # remove the biggest group gaps(k-1) cuts to yield k grps
    for j in range(k-1):
        total -= diff[j]

    print(total)