# https://leetcode.com/problems/sum-of-square-numbers/description/
# 633. Sum of Square Numbers
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # colliding pointers

        # half the number
        right = int(c ** 0.5) + 1

        # two pointers
        # not pointing but being the left and right 
        left = 0

        while right >= left:
            curr = left ** 2 + right ** 2

            if curr == c:
                return True
            elif curr > c:
                right -= 1
            else:
                left += 1

        return False
