t = int(input())

for _ in range(t):
    s = input()
    z_cnt = s.count("0")
    one_cnt = s.count("1")
    if z_cnt == one_cnt:
        print(z_cnt - 1)
        continue
    print(min(z_cnt, one_cnt))