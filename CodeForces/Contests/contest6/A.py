# https://codeforces.com/gym/677647/problem/A
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    tot = [0] * k
    mx = 0

    for _ in range(k):
        b, c = list(map(int, input().split()))
        tot[b-1] += c
        mx = max(mx, tot[b-1])
    

    # print(tot)
    ans = [0] * (mx + 1)  # got too big i guess

    for i in tot:
        if i != 0:
            ans[i] += 1
    
    last = 0

    for j in range(mx, -1, -1):
        if n == 0:
            break

        while n > 0 and ans[j]:
            last += j

            n -= 1
            ans[j] -= 1
    print(last)
