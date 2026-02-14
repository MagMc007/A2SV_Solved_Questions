t = int(input())
for _ in range(t):
    n = int(input())

    i = 2
    n -= 1

    alice = [1, 0]
    bob = [0, 0]

    odd_encountered = 1

    turn = 0

    while n >= i:
        # all evens fall here
        if turn % 2 == 0:  # bobs
            bob[0] += i // 2
            bob[1] += i // 2
            
        else:
            alice[0] += i // 2
            alice[1] += i // 2

        n -= i
        i += 1

        # all odds fall here
        if n >= i:
            if turn % 2 == 0:
                if odd_encountered % 2 == 0:
                    bob[0] += i // 2 + 1
                    bob[1] += i // 2
                else:
                    bob[0] += i // 2
                    bob[1] += i // 2 + 1
                n -= i
            else:
                if odd_encountered % 2 == 0:
                    alice[0] += i // 2 + 1
                    alice[1] += i // 2
                else:
                    alice[0] += i // 2
                    alice[1] += i // 2 + 1
                n -= i
            odd_encountered += 1
            i += 1
            turn += 1
        else:
            break

    if n:
        if n % 2 == 0:
            if turn % 2 == 0:
                bob[0] += n // 2
                bob[1] += n // 2
            else:
                alice[0] += n // 2
                alice[1] += n // 2
        else:
            if odd_encountered % 2 == 0:
                if turn % 2 == 0:
                    bob[0] += n // 2 + 1
                    bob[1] += n // 2
                else:
                    alice[0] += n // 2 + 1
                    alice[1] += n // 2
            else:
                if turn % 2 == 0:
                    bob[0] += n // 2 
                    bob[1] += n // 2 + 1
                else:
                    alice[0] += n // 2 
                    alice[1] += n // 2 + 1

    print(*alice, *bob)



""""
My mistake was not looking into the first on as 
an easy question
I was jumping question to question, not knowing which to
Solve 
& that costed me alot 

"""