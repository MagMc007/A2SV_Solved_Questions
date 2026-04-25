n = int(input())
ax, ay = map(int, input().split())  # queen
b = list(map(int, input().split()))  # king
c = list(map(int, input().split()))


dxns = [(-1, 0), (1, 0), (0, 1), (0, -1),
        (-1, -1), (1, 1), (-1, 1), (1, -1)
        ]


# queen divides all into quadrants
def qudrant(p1):
    x1, y1 = p1

    if x1 < ax:
        if y1 > ay:
            return "1"
        elif y1 < ay:
            return "4"
    else:
        if y1 > ay:
            return "2"
        elif y1 < ay:
            return "3"

    
if qudrant(b) == qudrant(c):
    print("YES")
else:
    print("NO")