# https://codeforces.com/gym/671638/problem/B
t = int(input())
for _ in range(t):
    m, s = map(int, input().split())
    b = list(map(int, input().split()))
    sum_ = sum(b)
    total = s + sum_

    root = (-1 + (1 + (8 * total)) ** 0.5) / 2
    print(root)
    if root == int(root):
        total_sum = (root * (root + 1)) / 2.0
        # print(total_sum)

        if total_sum == total:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


# t = int(input())

# for _ in range(t):
#     m, s = map(int, input().split())
#     b = list(map(int, input().split()))

#     max_ = max(b)
#     sum_ = sum(b)

#     sum_2_max = (max_ * (max_ + 1)) / 2  
#     # print(sum_2_max) 
#     left_out = sum_2_max - sum_
#     s -= left_out
#     max_ += 1

#     while s > 0:
#         s -= max_
#         max_ += 1
    
#     if s == 0:
#         print("YES")
#     else:
#         print("NO")
