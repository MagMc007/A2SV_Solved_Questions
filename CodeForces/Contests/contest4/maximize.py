t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)

    ans = 0
    i = 0
    j = 1

    while j < len(nums):
        ans += min(nums[i], nums[j])
        j += 2
        i += 2

    print(ans)
    
