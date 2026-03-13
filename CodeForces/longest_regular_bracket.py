# https://codeforces.com/problemset/problem/5/C
# C. Longest Regular Bracket Sequence
parenth = input()
n = len(parenth)

stack = []

max_ = 0
cnt = 0

for i in range(n):
    if parenth[i] == "(":
        stack.append(i)
    else:
        if not stack or parenth[stack[-1]] == ")":
            stack.append(i)
            continue
        
        idx = stack.pop()
        if stack:
            sub_leng = i - stack[-1] 
        else:
            sub_leng = i + 1
        
        if sub_leng == max_:
            cnt += 1
        elif sub_leng > max_:
            cnt = 1
            max_ = sub_leng

if max_ == 0:
    print("0 1")
else:
    print(max_, cnt)


