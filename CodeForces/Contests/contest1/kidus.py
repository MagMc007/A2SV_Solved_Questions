t = int(input())

for _ in range(t):
    combined = input()
    output = []

    for i in range(len(combined)):
        a = combined[:i]
        b = combined[i:]
        if a and b:
            if not a.startswith("0") and not b.startswith("0"):
                if int(a) < int(b):
                    output = [a, b]  
    if not output:
        print(-1)
    else:
        print(output[0], output[1])

    