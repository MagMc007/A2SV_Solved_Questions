# https://codeforces.com/problemset/problem/780/B
# B. The Meeting Place Cannot Be Changed

def check(time):
    first_spe = coord_spe[0][1]
    first_coor = coord_spe[0][0]

    rang = [first_coor - first_spe*time, first_coor + first_spe*time]

    for i in range(1, n):
        i_spe = coord_spe[i][1]
        i_coor = coord_spe[i][0]

        i_rang = [i_coor - i_spe*time, i_coor + i_spe*time]

        if i_rang[0] > rang[1]:
            return False
        
        rang = [max(i_rang[0], rang[0]), min(i_rang[1], rang[1])]
    
    return True


n = int(input())

coord = list(map(int, input().split()))
speeds = list(map(int, input().split()))

ans = -1 
low = 0
high = max(coord) - min(coord)
coord_spe = list(zip(coord, speeds))
coord_spe.sort()

while high - low > 10 ** -6:
    mid = (high + low) / 2

    if check(mid):
        ans = mid
        high = mid
    else:
        low = mid

print(ans)

'''
time: nlogn
space: O(n)
'''