# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
# 442. Find All Duplicates in an Array
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set() # output space

        for num in nums:  # O(n)
            #remove those that are repeated
            if num in res:  
                res.remove(nums) # O(1)
            else:
                res.add(num)
        
        # symetric diffence
        return list(res ^ set(nums)) # space O(n)
    

# violated the contriant
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        # length is n, [1, n] given so use the numbers themselves 
        # as an index to mark as seen or not
        # all are positive so make them -ve to mark
        # use the index

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1

            if nums[idx] < 0:
                res.append(abs(nums[i]))
            else:
                nums[idx] = -1 * nums[idx]
                
        return res