# https://codeforces.com/gym/671638/problem/B

t = int(input())

for _ in range(t):
    m, s = map(int, input().split())
    b = list(map(int, input().split()))

    max_ = max(b)
    sum_ = sum(b)

    sum_2_max = (max_ * (max_ + 1)) / 2  
    # print(sum_2_max) 
    left_out = sum_2_max - sum_
    s -= left_out
    max_ += 1

    while s > 0:
        s -= max_
        max_ += 1
    
    if s == 0:
        print("YES")
    else:
        print("NO")
