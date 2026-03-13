# https://leetcode.com/problems/lemonade-change/
# 860. Lemonade Change
from collections import Counter

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        hash = Counter()  # only 5 and 10

        # bills.sort() # in queue so no changing

        for bill in bills:
            if bill == 5:
                hash[5] += 1
            
            if bill == 10:
                if hash[5] == 0:
                    return False
                
                hash[5] -= 1
                hash[10] += 1

            if bill == 20:
                curr = 15 
                # give back in 10
                if hash[10] > 0:
                    curr -= 10
                    hash[10] -= 1
                
                times = curr // 5
                if hash[5] >= times:
                    curr -= 5 * times
                    hash[5] -= times
                    continue
                
                return False
        return True
                    
print(Solution().lemonadeChange([5,5,5,20,10,10]))