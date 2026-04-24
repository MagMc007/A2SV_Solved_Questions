# https://codeforces.com/problemset/problem/2056/B
# B. Find the Permutation
from collections import defaultdict
t = int(input())

for _ in range(t):
    hash = defaultdict(int)

    n = int(input())
    mtx = [] 

    for _ in range(n):
        row = [int(num) for num in input()]
        mtx.append(row)
    # print(mtx)
    
    left = 0
    right = n - 1

    for row in range(n-2, -1, -1):
        for col in range(n):
            # print(hash)
            if row < col and mtx[row][col] == 1:
                if row+1 not in hash:
                    hash[row+1] = left
                    left += 1

                if col + 1 not in hash:
                    hash[col+1] = right
                    right -= 1
                else:
                    if hash[row+1] > hash[col+1]:
                        hash[row+1], hash[col+1] = hash[col+1], hash[row+1]
    
    if len(hash) < n:
        print(*[i for i in range(n, 0, -1)])
    else:
        ans = [0] * n
        
        for k, v in hash.items():
            ans[v] = k
        
        print(*ans)









    
