t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = []
    
    # flatten as u go
    for i in range(n):
        ls = list(map(int, input().split()))
        a.extend(ls)
    
    if len(a) == 1:
        print(-1)
        continue
    
    elm = a.pop()
    a.insert(0, elm)
    # at m steps construct the arr
    start = 0
    end = m
    for _ in range(n):
        print(*a[start:end])
        start += m
        end += m

