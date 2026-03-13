# https://codeforces.com/problemset/problem/5/C
# C. Longest Regular Bracket Sequence
parenth = input()
n = len(parenth)

stack = [-1]  # -1 will act as a wall

sub_seq_len = 0
cnt = 0

for i in range(n):
    if i == "(":
        stack.append(i)
    else:
        stack.pop()

        if not stack:
            stack.append(i)
        else:
            length = i - stack[-1]

            if length > max_len:
                max_len = length
                count = 1
            elif length == max_len:
                count += 1

if max_len == 0:
    print(0, 1)
else:
    print(max_len, count)