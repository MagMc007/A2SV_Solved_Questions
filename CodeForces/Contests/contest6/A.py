# https://codeforces.com/gym/677647/problem/A
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    tot = [0] * (k+1)
 
    for _ in range(k):
        b, c = map(int, input().split())
        tot[b] += c
  
    tot.sort(reverse=True)
    print(sum(tot[:n]))