# https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/C
# C. Number of Segments with Small Sum
n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
curr_sum = 0
left = 0

for right in range(n):
    curr_sum += arr[right]

    while curr_sum > m:
        curr_sum -= arr[left]
        left += 1

    cnt += right - left + 1
    
print(cnt)