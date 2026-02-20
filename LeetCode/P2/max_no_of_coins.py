# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/
# 1561. Maximum Number of Coins You Can Get
class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort(reverse=True)

        n = len(piles)
        
        # how many am i taking ??
        times = n // 3
        output = 0

        # to maximize you coins, bob needs to take the lowest 
        # possible coins
        # smalles n coins belong to bob
        for i in range(1, times * 2, 2):
            output += piles[i]
        
        return output
 
soln =  Solution()
print(soln.maxCoins([9,8,7,6,5,1,2,3,4]))