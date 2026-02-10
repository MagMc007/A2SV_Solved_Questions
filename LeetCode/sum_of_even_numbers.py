# https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/
# 985. Sum of Even Numbers After Queries

class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
            first store the sum of the even numbers from num
            in a variable
            after that for each iteration check if the existing 
            number at the index is even or odd and modify the answer you stored
            (number even so already considered so subtract it from ans
            if odd then move on and do operation)
            after the operation if the number we have at that index is evn 
            add it to ans and append it
            else append the existing ans
        """
        # get the sum of the evens
        answer = []
        ans = 0
        for i in nums:
            if i % 2 == 0:
                ans += i
        
        for val, idx in queries:
            if nums[idx] % 2 == 0:  # if the number was even sub from ans
                ans -= nums[idx]

            nums[idx] = nums[idx] + val
            if nums[idx] % 2 == 0:
                ans += nums[idx]
            answer.append(ans)
        return answer
    
soln = Solution()
print(soln.sumEvenAfterQueries(nums = [1], queries = [[4,0]]))