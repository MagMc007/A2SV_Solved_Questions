# https://codeforces.com/problemset/problem/1504/B
# B. Flip the Bits
t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    
    # add extra char & check i+1
    a += '0'
    b += '0'
    
    zeros = ones = 0
    ok = True
    
    for i in range(n):
        if a[i] == '0':
            zeros += 1
        else:
            ones += 1
        
        same_now = (a[i] == b[i])
        same_next = (a[i + 1] == b[i + 1])
        
        if same_now != same_next:
            if zeros != ones:
                ok = False
                break
    
    print("YES" if ok else "NO")


