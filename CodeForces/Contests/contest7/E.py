n = int(input())
s = input()
 
ans = []
 
i = 0
j = 1
dels = 0
 
while j < n:
    if s[i] != s[j]:
        ans.append(s[i])
        ans.append(s[j])
        i = j + 1
        j += 2
    else:
        j += 1
        dels += 1
 
if i < n:
    ans.append(s[i])   
    
if len(ans) % 2 == 0:
    print(dels)
    print("".join(ans))
else:
    ans.pop()
    print(dels + 1)
    print("".join(ans))