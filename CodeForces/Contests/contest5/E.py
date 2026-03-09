# Read number of test cases
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # get those a[i] < i+1
    is_good = [0] * (n + 1)

    for i in range(n):
        if a[i] < i + 1:
            is_good[i + 1] = 1
 
    pref = [0] * (n + 1)
    for k in range(1, n + 1):
        pref[k] = pref[k-1] + is_good[k]
        
    # 3. Count the valid pairs
    ans = 0
    for idx in range(n):
        val = a[idx]
        j = idx + 1 
        
        if is_good[j]:
            condition_limit = val - 1
            
            if condition_limit > 0:
                if condition_limit > n:
                    condition_limit = n
                
                ans += pref[condition_limit]
    
    print(ans)