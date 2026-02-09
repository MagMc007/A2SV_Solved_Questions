# https://leetcode.com/problems/integer-to-roman/description/
# 12. Integer to Roman
class Solution:
    def intToRoman(self, num: int) -> str:
        romans = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        roman_number = ""

        for integer, roman in romans:
            if num == 0:  # by the time we reach the last digit we break
                break

            quotient = num // integer  # how many times
            roman_number += str(roman) * quotient
            num -= quotient * integer

        return roman_number


        

    
soln = Solution()
print(soln.intToRoman(1994))



