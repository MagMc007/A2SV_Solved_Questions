# https://codeforces.com/gym/676872/problem/A
t = int(input())

for _ in range(t):
    word = input()
    print(word + word[::-1])

    