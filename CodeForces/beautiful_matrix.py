# https://codeforces.com/problemset/problem/263/A
# A. Beautiful Matrix
entry = []
idx = []
for i in range(5):
    row = input().split()
    if "1" in row:
        idx = [i + 1, row.index("1") + 1]
    entry.append(row)

# middle is (3,3)
print(abs(3 - idx[0]) + abs(3-idx[1]))


