n, k = map(int, input().split())
 
layers = list(input())
layers.sort()
# print(layers)
curr = ord(layers[0]) - 96
s = curr
k -= 1
 
# print(curr)
 
for i in range(1, n):
    if not k:
        break
 
    c = ord(layers[i]) - 96
    if c >= curr + 2:
        # print(layers[i])
        s += c
        # print(curr)
        curr = c
        k -= 1
 
if k:
    print(-1)
else:
    print(s)