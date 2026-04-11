t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    s = input()
    w = input()
    
    target_sum = 0
    for char in w:
        target_sum += ord(char)
        
    # get the ASCII
    s_vals = [ord(c) for c in s]
    
    curr_window = 0
    for i in range(m):
        curr_window += s_vals[i]
        
    found = False
    if curr_window == target_sum:
        found = True
    else:
        for i in range(m, n):
            curr_window += s_vals[i] - s_vals[i - m]
            if curr_window == target_sum:
                found = True
                break
    
    if found:
        print("YES")
    else:
        print("NO")
