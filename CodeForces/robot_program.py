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
    
