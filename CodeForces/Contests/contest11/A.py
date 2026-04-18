n = int(input())
nums = list(map(int, input().split()))

nums.sort()

ans = 0
i = 0
j = n-1
while i < j:
    ans += (nums[i] + nums[j]) ** 2
    j -= 1
    i += 1
print(ans)
