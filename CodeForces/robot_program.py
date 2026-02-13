# https://codeforces.com/problemset/problem/2070/B
# B. Robot Program
t = int(input())
for _ in range(t):
    # n - number of commands
    # x - starting point
    # k - seconds in w/c robot passes through 0
    n, x, k = map(int, input().split())
    commands = input()

    cmd_pairing = {"L": -1, "R": 1}

    passes_0 = 0
    i = 0

    # command complete or time ran out, stop the loop
    while i < n and k > 0:
        # move the robot
        x += cmd_pairing[commands[i]]

        # go to the next command
        i += 1

        # if robot is @ 0
        if x == 0:
            i = 0
            passes_0 += 1
        k -= 1
    
    print(passes_0)

