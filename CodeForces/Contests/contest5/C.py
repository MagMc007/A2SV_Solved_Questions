t = int(input())

for _ in range(t):
    w = list(input())
    p = int(input())

    n = len(w)
    s = 0
    pair = []

    for i in range(n):
        w[i] = ord(w[i])
        s += w[i] - 96
        pair.append([w[i], i])
        
    
    # print(w)
    # print(s)

    if s <= p:
        w = list(map(chr, w))
        print("".join(w))
        continue
  
    pair.sort(reverse=True) # biggest at first
    # print(pair)


    i = 0
    while s > p and i < n:
        # print(pair[i][0] - 96)
        # print(chr(pair[i][0]))
        s -= pair[i][0] - 96
        i += 1
        # print(s)

    if i == n:
        print()
        continue

    ans = [0] * n

    for j in range(i, n):
        asc, idx = pair[j]
        ans[idx] = asc
    
    # print(ans)
    
    res = ""
    for i in ans:
        if i != 0:
            res += chr(i)
    print(res)


    








