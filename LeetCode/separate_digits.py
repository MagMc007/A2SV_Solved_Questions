# https://leetcode.com/problems/separate-the-digits-in-an-array/description/
# 2553. Separate the Digits in an Array
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        # just change to string and keep on appending
        output = []

        for i in nums:
            for j in str(i):
                output.append(int(j))
        return output