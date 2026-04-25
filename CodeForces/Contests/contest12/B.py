t = int(input())

for _ in range(t):
    n = int(input())
    
    line1 = list(input())
    line2 = input()

    moves = 0

    for i in range(n):
        if line2[i] == '1':
            if line1[i] == '0':
                moves += 1
                line1[i] = 'p'
            elif i-1 >= 0 and line1[i-1] == '1':
                line1[i-1] = 'p'
                moves += 1
            elif i+1 < n and line1[i+1] == '1':
                moves += 1
                line1[i+1] = 'p'
    # print(line1)
    print(moves)


