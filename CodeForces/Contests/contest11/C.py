from collections import Counter, defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = Counter(a)
stat = True

for key, v in cnt.items():
    if v > k:
        stat = False

if not stat:
    print("NO")
else:
    labeled = defaultdict(set)
    ans = []

    n = 1

    for i in a:
        if i not in labeled[n % k]:
            if n % k == 0:
                # print(n, k)
                ans.append(k)
            else:
                ans.append(n % k)

            labeled[n % k].add(i)
            n += 1
        else:
            while i in labeled[n % k]:
                n += 1

            if n % k == 0:
                ans.append(k)
            else:
                ans.append(n % k)

            labeled[n % k].add(i)
            
    print("YES")
    print(*ans)
    

            

            

    
