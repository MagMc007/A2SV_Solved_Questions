t = int(input())

for _ in range(t):
    s = input()
    removed = 0

    i = 0
    checker = set()

    while i < len(s):
        # print(checker)
        # print(len(checker))
        if s[i] in checker:
            removed += len(checker) - 1
            checker = set()
            i += 1
            continue
        
        checker.add(s[i])
        i += 1

    removed += len(checker)

    print(removed)


    