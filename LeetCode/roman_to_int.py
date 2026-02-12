# https://leetcode.com/problems/roman-to-integer/description/
# 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # on commond thing the constriats have is that
        # the next number is less than the other
        # IV in out case when reversed will be - VI
        # V > I ; same for all of them

        # start from the back so we reverse
        s = s[::-1]
        output = vals[s[0]]

        for i in range(len(s)-1):
            if vals[s[i]] > vals[s[i+1]]:
                output -= vals[s[i+1]]
            else:
                output += vals[s[i+1]]
        return output