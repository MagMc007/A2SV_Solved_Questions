# https://leetcode.com/problems/product-of-array-except-self/description/
# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prod = 1
        is_zero = 0

        for i in nums:
            if i != 0:
                prod *= i
            else:
                is_zero += 1
        
        res = []

        for i in nums:
            if not is_zero:
                res.append(prod // i)
            else:  # there is a zero
                if i == 0:
                    if is_zero == 1:
                        res.append(prod)
                    else:
                        res.append(0)
                else:
                    res.append(0)
                    
        return res
    
# print(Solution().productExceptSelf([-1,0,1,0,-3,3]))

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # do the suffix
        suffx_prod = [nums[-1]]

        for j in range(len(nums)-2, -1, -1):
            # print(suffx_prod)
            curr = [suffx_prod[0] * nums[j]]
            curr.extend(suffx_prod)
            suffx_prod = curr
            
        # do the prefix product
        pref_prod = 1
        res = []
        arr = []
        for i in range(len(nums)):
            pref_prod *= nums[i]
            arr.append(pref_prod)

            if i == 0:
                res.append(suffx_prod[i+1])
            elif i == len(nums) - 1:
                res.append(arr[i-1])
            else:
                res.append(suffx_prod[i+1] * arr[i-1])

        return res

print(Solution().productExceptSelf([1,2,3,4]))
