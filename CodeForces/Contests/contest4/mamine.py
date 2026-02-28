n, k = map(int, input().split())
a = list(map(int, input().split()))

pairing = []

for i in range(n):
    pairing.append([a[i], i+1])

# sort them based on the gap they have from k
pairing.sort(key=lambda x: x[0] - k)


# print(pairing)

ans = []
curr = 0

for val, idx in pairing:
    curr += val
    if curr > k:
        break

    ans.append(idx)
if ans:
    print(len(ans))
    print(*ans)
else:
    print(0)
"""
 I have completely missed the approach here
 i was thinking sliding window but it is not
 it requires sorting ...
"""