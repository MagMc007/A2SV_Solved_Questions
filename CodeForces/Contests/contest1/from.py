from collections import Counter

q = int(input())
for _ in range(q):
    s = input()
    t = input()
    p = input()
    
    pcnt = Counter(p)
    scnt = Counter(s)

    flag = True
    orderS = 0
    orderP = 0

    for i in range(len(t)):
        if scnt.get(t[i]):
            if t[i] != s[orderS]:
                flag = False
                break
            scnt[t[i]] -= 1
            orderS += 1
        else:
            if pcnt.get(t[i]):
                pcnt[t[i]] -= 1
                orderP += 1
            else:
                flag = False
        
    if flag:
        print('YES')
    else:
        print("NO")







