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
for s, c in comp:
    if sum_ <= m:
        break
    else:
        sum_ -= s - c
        times += 1


if times < n:
    print(times)
else:
    print(-1)

