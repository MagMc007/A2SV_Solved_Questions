n, k = map(int, input().split())

path = input()

jump = 0
flag = True
for i in range(n):
    if path[i] == "#":
        jump += 1
    else:
        jump = 0
    
    if jump >= k:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
        