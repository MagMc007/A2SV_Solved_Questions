n, m = map(int, input().split())
 
files = {}
comp = []
sum_ = 0
 
for _ in range(n):
    a, b = map(int, input().split())
    sum_ += a
    files[(a, b)] = a - b
        
    comp.append([a, b])
 
comp.sort(key=lambda x: files[tuple(x)], reverse=True)
# print(sum_)
# print(comp)
times = 0
for s, c in comp:
    if sum_ <= m:
        break
    else:
        sum_ -= s - c
        times += 1
        
if sum_ > m:
    print(-1)
else:
    print(times)