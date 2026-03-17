# https://leetcode.com/problems/count-good-numbers/description/
# 1922. Count Good Numbers
class Solution:
    def myPow(self, x: float, n: int) -> float:
        MOD = 7 + 10 ** 9
        # halving into 2 is prefered instead of going one by one
        # base cases
        if n == 0:
            return 1
        
        if n % 2 == 0:
            half = self.myPow(x, n // 2) % MOD
            return (half * half) % MOD
        else:
            return x * self.myPow(x, n-1)
        
    def countGoodNumbers(self, n: int) -> int:
        # don't decrease one by one, 
        # do separately, 5 separately by using power
        # 4 separately by using power
        MOD = 7 + 10 ** 9
        if n % 2 == 0:
            evens = self.myPow(5, n//2) % MOD
            odds = self.myPow(4, n // 2) % MOD
        else:
            evens = self.myPow(5, (n+1)//2) % MOD
            odds = self.myPow(4, n//2) % MOD
        return (evens * odds) % MOD
        


print(Solution().countGoodNumbers(4))