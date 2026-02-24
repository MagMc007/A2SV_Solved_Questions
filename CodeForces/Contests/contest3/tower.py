n = int(input())


towers = [] # [(len, blocks)]
numbers = [] # sort later for indexing

for _ in range(n):
    block = list(map(int, input().split()))
    k, block = block[0], block[1:]
    numbers.extend(block)

    towers.append((k, block))

numbers.sort()

hash = {}
for i in range(len(numbers)):
    hash[numbers[i]] = i
splits = 0
blocks = len(towers)

for tow in towers:
    leng, bl = tow
    prev = hash[bl[0]]

    for j in range(1, leng):
        # current_idx - prev_id = 1(0 in the case of the start)
        if hash[bl[j]] - prev != 1:
            splits += 1

        prev = hash[bl[j]]

print(splits, splits + len(towers) -1)
        




