# https://codeforces.com/gym/671638/problem/E
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    # n - rows  m - cols

    matrix = []

    for _ in range(n):
        row = input()
        matrix.append(row) 

    # boundaries
    top = 0
    left = 0
    right = m
    bottom = n

    count = 0

    for l in range(min(n, m) // 2):
        block = ""
        j = l
        i = l

        # move right
        while j < right:
            block += matrix[i][j]
            j += 1

        j -= 1
        i += 1
        right -= 1

        # move down
        while i < bottom:
            block += matrix[i][j]
            i += 1

        i -= 1
        j -= 1
        bottom -= 1

        # move left
        while j >= left:
            block += matrix[i][j]
            j -= 1
        
        left += 1
        j += 1
        i -= 1

        # move up
        while i > top:
            block += matrix[i][j]
            i -= 1
        top += 1
        
        block = block + block[:3]
        count += block.count("1543")        
        # print(block)
    print(count)