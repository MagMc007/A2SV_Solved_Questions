# https://codeforces.com/gym/671638/problem/D
t = int(input())

for _ in range(t):
    m = int(input())

    matrix = []
    for _ in range(m):
        row = list(input())
        matrix.append(row)
    swaps = 0
    # print(matrix)

    # per iteration we're supposeto have 4 swapping
    # we compare the 4 in this case

    cols = len(matrix)
    n = cols - 1

    for i in range(cols // 2):
        for j in range(cols - 1):
            cell1 = int(matrix[i][i+j])
            cell2 = int(matrix[i+j][n-i])
            cell3 = int(matrix[n-i][n-j-i])
            cell4 = int(matrix[n-i-j][i])

            # print(cell1, cell2, cell3, cell4)
            sum_ = cell1 + cell2 + cell3 + cell4

            if sum_ == 0 or sum_ == 4:  # no swaps needed
                continue
            elif sum_ == 3 or sum_ == 1:
                swaps += 1
            else:  # 2
                swaps += 2
        cols -= 2
   

    print(swaps)