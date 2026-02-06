# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
# 442. Find All Duplicates in an Array
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        # no hash maps, restricted by the constriant

        output = set()  # excluded space

        for num in nums:
            if num in output:
                output.remove(num)
            else:
                output.add(num)
                
        return list(output ^ set(nums))
    

soln = Solution()
print(soln.findDuplicates([4,3,2,7,8,2,3,1]))     