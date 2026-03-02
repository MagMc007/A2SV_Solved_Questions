# https://codeforces.com/problemset/problem/1364/B
# B. Most socially-distanced subsequence
t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    output = [p[0]]

    for i in range(1, n):
        if i < n-1:
            if p[i-1] < p[i] > p[i+1] or p[i-1] > p[i] < p[i+1]:
                output.append(p[i])
    output.append(p[-1])

    print(len(output))
    print(*output)
        
        