# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        ctr = Counter(nums)

        nums.sort(key=lambda x: ctr[x], reverse=True)
        # print(nums)
        output = set()
        for num in nums:
            if k:
                if num not in output:
                    output.add(num)
                    k -= 1
            else:
                break

        return list(output)