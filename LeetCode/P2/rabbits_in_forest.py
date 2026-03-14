# https://leetcode.com/problems/rabbits-in-forest/description/
# 781. Rabbits in Forest
from collections import Counter


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hash = Counter(answers)
        min_cnt = 0

        for k, val in hash.items():
            while val > 0:
                min_cnt += k + 1
                val -= k + 1
            
        return min_cnt



