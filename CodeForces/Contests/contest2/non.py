# https://codeforces.com/gym/671638/problem/A1
t = int(input())
for _ in range(t):
    n = int(input())

    bob = [0, 0]
    alice = [0, 0]

    turn = 0

    for i in range(0, n // 2, 2):
        if n < i:
            break

        if turn % 2 == 0:
            alice += i
            n -= i
        else:
            bob += i
            n -= i

        if n > i + 1:
            if turn % 2 == 0:
                alice += i + 1
                n -= i + 1
            else:
                bob += i + 1
                n -= i + 1
            turn += 1
        else:
            break

    if n:
        if turn % 2 == 0:
            alice += n
        else:
            bob += n
                
    print(alice, bob)
            
        








