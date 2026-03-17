# https://leetcode.com/problems/fibonacci-number/description/
# 509. Fibonacci Number

# state: look for the Fib of n
# base case: if n == 0 and n == 1
# RR: adding the previous 2

class Solution:
    def fib(self, n: int) -> int:
        # base case
        if n == 0:
            return 0
        
        if n == 1:
            return 1
    
        return self.fib(n-1) + self.fib(n-2)