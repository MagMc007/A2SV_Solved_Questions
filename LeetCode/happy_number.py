# https://leetcode.com/problems/happy-number/description/?envType=problem-list-v2&envId=hash-table
# 202. Happy Number
# 202. Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        """
            there will be an endless loop
            but if you reach one you chould break 
            if not continue untill you have a repeated
            number from the previous iteration

        """
        visited = set()
        summed = 0

        n = str(n)
        while summed != 1:
            summed = 0
            for i in n:
                summed += (int(i)) ** 2
            # check if it is in the previous sums
            if summed in visited:
                return False
            # add it if it not
            visited.add(summed)
            # change n to str of summed & init summed to 0
            n = str(summed)
            
        return True

soln = Solution()
print(soln.isHappy(2))