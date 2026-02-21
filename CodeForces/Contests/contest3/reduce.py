n, m = map(int, input().split())

comp = []
sum_ = 0

for _ in range(n):
    a, b = map(int, input().split())
    sum_ += a
    comp.append(a-b)
comp.sort(reverse=True)

# sorted based on difference in desc order
# print(comp)
times = 0
for s in comp:
    if sum_ <= m:
        break
    else:
        sum_ -= s
        times += 1

# sum may be greater than m
if sum_ <= m and times != n:
    print(times)
else:
    print(-1)

"""
My problem was i did not conside if the compressed files 
would not even fit in
"""