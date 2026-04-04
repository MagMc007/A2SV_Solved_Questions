t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    first = a.pop()

    a.sort()

    print(first + a[-1])