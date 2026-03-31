t = int(input())

for _ in range(t):
    n = int(input())
    sticks = list(map(int, input().split()))
    
    counts = [0] * 101
    for leng in sticks:
        counts[leng] += 1
    
    ans = 0

    for stick_cnt in counts:
        ans += stick_cnt // 3
        
    print(ans)