# from collections import Counter

# q = int(input())
# for _ in range(q):
#     s = input()
#     t = input()
#     p = input()
    
#     pcnt = Counter(p)
#     scnt = Counter(s)

    # flag = True
    # orderP = 0  # number of elements added from p

    # for i in range(len(t)):
    #     if scnt.get(t[i]):  # in s
    #         if t[i] != s[i - orderP]:
    #             flag = False
    #             break
    #         scnt[t[i]] -= 1
    #     elif pcnt.get(t[i]):  # in p
    #         if pcnt[t[i]]:  # must be greater than 0
    #             pcnt[t[i]] -= 1
    #             orderP += 1
    #         else:
    #             flag = False
    #             break
    #     else:
    #         flag = False
    #         break
        
    # if flag:
    #     print('YES')
    # else:
    #     print("NO")


"""
    Analysis: Check for subsequence, 
                then check if the elements in T can be provided by the
                sum of count of elements in s and p
"""

def isSubseq(s, t):
    ptr1 = 0
    ptr2 = 0

    while ptr1 < len(s) and ptr2 < len(t):
        if s[ptr1] == t[ptr2]:
            ptr1 += 1
            ptr2 += 1
        else:
            ptr2 += 1
    
    return ptr1 == len(s)
        

def satisfy(s, t, p):
    pcnt = Counter(p)
    scnt = Counter(s)
    tcnt = Counter(t)

    for i in t:
        if tcnt[i] > scnt.get(i, 0) + pcnt.get(i, 0):
            return False
    return True


from collections import Counter

q = int(input())
for _ in range(q):
    s = input()
    t = input()
    p = input()

    if satisfy(s, t, p) and isSubseq(s, t):
        print("YES")
    else:
        print("NO")

    
    

    



