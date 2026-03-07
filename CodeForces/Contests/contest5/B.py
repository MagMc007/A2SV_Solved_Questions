t = int(input())

for _ in range(t):
    n = int(input())
    dig = input()

    # all i need is 2 odds, get rid of the rest
    # the number will be odd and add up to be even
    odds = ""
    for i in dig:
        if len(odds) == 2:
            break

        if int(i) % 2 != 0:
            odds += str(i)

    if len(odds) < 2:
        print(-1)
    else:
        print(odds)


    # digs = list(map(int, dig))
    # s = sum(digs)

    # i = -1

    # # make the number odd
    # while s and digs[-1] % 2 == 0:
    #     s -= digs.pop()
    #     n -= 1

    # # print(digs)
    # if not s:
    #     print(-1)
    #     continue


    
    # # make the sum even
    # last = digs.pop() # it is odd
    # s -= last

    # # now the rem must be odd 
    # while digs and s % 2 == 0:
    #     s -= digs.pop()

    # s += last
    # digs.append(last)
    # print(s)

    # if dig and s % 2 == 0:
    #     # print(digs)
    #     digs = list(map(str, digs))
    #     print("".join(digs))
    #     continue
    # else:
    #     print(-1)
    #     continue

    
    
