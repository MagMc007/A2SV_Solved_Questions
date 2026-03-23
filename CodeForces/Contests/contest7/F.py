from collections import defaultdict, deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))

length = defaultdict(list)

min_q = deque()
max_q = deque()

left = 0

for r in range(n):
    while min_q and min_q[-1] > arr[r]:
        min_q.pop()

    min_q.append(arr[r])

    while max_q and max_q[-1] < arr[r]:
        max_q.pop()

    max_q.append(arr[r])

    # check the max and min
    while max_q[0] - min_q[0] > k:
        if min_q[0] == arr[left]:
            min_q.popleft()
        
        if max_q[0] == arr[left]:
            max_q.popleft()

        left += 1

    curr_len = r - left + 1
    length[curr_len].append([left+1, r+1])


max_leng = max(length)
cnts = len(length[max_leng])

print(max_leng, cnts)
for i in range(cnts):
    print(*length[max_leng][i])

