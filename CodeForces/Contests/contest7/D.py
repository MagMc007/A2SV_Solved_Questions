# https://codeforces.com/gym/680006/problem/D
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    if m >= n:
        print("NO")
        continue

    stat = False

    while n > 0:
        curr = n / 3

        dbl = curr * 2

        if m in [curr, dbl]:
            stat = True
            break

        n = dbl
    
    if stat:
        print("YES")
    else:
        print("NO")

    



        
