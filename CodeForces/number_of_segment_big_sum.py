# https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/D
# D. Number of Segments with Big Sum
n, m = map(int, input().split())
arr = list(map(int, input().split()))

curr_sum = 0
cnt = 0
left = 0

for right in range(n):
    curr_sum += arr[right]
    
    while curr_sum >= m:
        cnt += (n - right)
        curr_sum -= arr[left]
        left += 1
    
print(cnt)