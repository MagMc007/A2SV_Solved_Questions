# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/
from collections import Counter


class Solution1:
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
    
# bucket sort
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ctr = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]

        for key, v in ctr.items():
            bucket[v].append(key)
        
        ans = []

        for i in range(len(bucket)-1, -1, -1):
            if not k:
                break

            for el in bucket[i]:
                ans.append(el)
                k -= 1
        
        return ans