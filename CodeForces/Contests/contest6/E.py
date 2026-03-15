t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    u = sorted(set(a))
    
    max_freq = 0
    left = 0
    
    for right in range(len(u)):
        
        while u[right] - u[left] >= n:
            left += 1
            
        curr_window = right - left + 1
        
        if curr_window > max_freq:
            max_freq = curr_window
            
    print(max_freq)