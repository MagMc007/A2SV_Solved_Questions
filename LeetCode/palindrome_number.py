class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False    

        digits = []  # store to compare later
        
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        
        if digits == digits[::-1]:
            return True
        return False
