# https://leetcode.com/problems/pancake-sorting/description/
# 969. Pancake Sorting
class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        flips = []
        sorted_arr = sorted(arr)

        # keep track of the biggest of the unsorted 
        biggest = max(arr)

        # the biggest needs to go to idx 0
        # then flipped to go to its correct position
        while arr != sorted_arr:
            # print(arr)
            idx = arr.index(biggest)

            # is it at its correct position??
            if idx + 1 == biggest:
                biggest -= 1
                continue

            # do the flipping
            left = arr[0:idx+1]
            left = left[::-1]
            right = arr[idx+1:]
            # print(left, right)
            arr = left + right
            # print(arr)
            flips.append(idx + 1)

            # now it is at the start, flip it to it correct posn
            left = arr[:biggest]
            left = left[::-1]
            right = arr[biggest:]
            arr = left + right
            # print(arr)
            flips.append(biggest)
            biggest -= 1
            # print(biggest)
            
        return flips   


soln = Solution()
print(soln.pancakeSort([3,2,4,1]))