# https://leetcode.com/problems/powx-n/description/
# 50. Pow(x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # halving into 2 is prefered instead of going one by one
        # base cases
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, abs(n))
        
        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        else:
            return x * self.myPow(x, n-1)


print(Solution().myPow(2.00000, 3))

# space: O(n)
# time: O(logn) // halfing by 2