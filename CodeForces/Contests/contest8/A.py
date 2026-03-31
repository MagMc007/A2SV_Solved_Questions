n = int(input())
item = input()

cntL = item.count('L')
cntO = item.count('O')

loaf_cnt = 0
onion_cnt = 0

ans = -1

for i in range(1, n):
    current_item = item[i - 1]
    
    if current_item == 'L':
        loaf_cnt += 1
    else:
        onion_cnt += 1
    
    
    friend_loaf_cnt = cntL - loaf_cnt
    friend_onion_cnt = cntO - onion_cnt
    
    if loaf_cnt != friend_loaf_cnt and onion_cnt != friend_onion_cnt:
        ans = i
        break

print(ans)