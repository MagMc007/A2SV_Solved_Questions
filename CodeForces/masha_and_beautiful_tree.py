# https://codeforces.com/problemset/problem/1741/D
# D. Masha and a Beautiful Tree
import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
t = int(input())

for _ in range(t):
    m = int(input())
    p = list(map(int, input().split()))

    # merge sort the array
    # should not go to the end(last element instead return when we have
    # 2 elements) guerantees the permutation is power of 2
    cnt = 0

    def mergeArrOf2(eleft, elright):
        global cnt

        if eleft > elright:
            cnt += 1
            return [elright, eleft]    
        
        return [eleft, elright]

    def checker(leftArr, rightArr):
        global cnt

        # can only compare the first elements
        if leftArr[0] > rightArr[0]:
            cnt += 1
            return rightArr + leftArr
        
        return False

    def mergeSort(left, right, arr):
        # base case
        # lenght must be 2
        if right - left + 1 == 2:
            return mergeArrOf2(arr[left], arr[right])
        
        mid = left + (right - left) // 2

        left = mergeSort(left, mid, arr)
        right = mergeSort(mid+1, right, arr)

        if left and right:
            return checker(left, right)
        return False
    
    ans = mergeSort(0, m-1, p)
    if ans:
        print(cnt)
    else:
        print(-1)
