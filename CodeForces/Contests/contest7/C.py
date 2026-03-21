
a, b = map(int, input().split())
 
ans = [b,]
 
while b > a:
    num = b % 10
 
    if num % 2 == 0: # multiplied
        b = b // 2
        ans.append(b)
    elif num == 1:  # was mult by 10 and 1 was added
        b -= 1
        b = b // 10
        ans.append(b)
    else:
        break
 
if b == a:
    print("YES")
    print(len(ans))
    print(*ans[::-1])
else:
    print("NO")