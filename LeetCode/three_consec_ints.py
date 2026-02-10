# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/description/
# 2177. Find Three Consecutive Integers That Sum to a Given Number
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        """
            the logic here is divide the number with 3
            no remainders
            now we can say that the number we got, the number before
            it and the number after it will add up to result the
            number
        """
        if num % 3 != 0:
            return []
        
        q = num // 3
        return [q-1, q, q + 1]