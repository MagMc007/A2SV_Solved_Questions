# https://leetcode.com/problems/boats-to-save-people/description/
# 881. Boats to Save People
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        arr = sorted(people)

        l = 0
        r = len(people) - 1

        boats = 0

        while l < r:
            if limit == arr[r]:
                boats += 1
                r -= 1
            elif arr[l] + arr[r] > limit:
                boats += 1
                r -= 1
            else:
                boats += 1
                r -= 1
                l += 1
        if l == r:
            boats += 1
        return boats