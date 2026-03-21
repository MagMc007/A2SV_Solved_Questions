# https://codeforces.com/gym/680006/problem/A
k = int(input())
 
arr = list(map(int, input().split()))
 
mx = max(arr)
if mx <= 25:
    print(0)
else:
    print(mx-25)