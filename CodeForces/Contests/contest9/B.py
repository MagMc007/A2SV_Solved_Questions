# # https://codeforces.com/gym/683262/problem/B
q = int(input())

for _ in range(q):
    n = int(input())
    nums = input()

    ans = [int(nums[0]),]
    # process ans
    i = 1

    curr = ""

    while i < n:
        curr += nums[i]

        # current number is greater
        if curr and int(curr) > ans[-1]:
            ans.append(int(curr))
            curr = ""

        i += 1

    if curr:
        j = ans.pop()
        j = str(j) + curr
        ans.append(int(j))
    if len(ans) < 2:
        print("NO")
    else:
        print("YES")
        print(len(ans))
        print(*ans)
