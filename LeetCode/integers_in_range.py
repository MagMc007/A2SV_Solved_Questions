class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        inclusive_range = {i for i in range(left, right + 1)}
        
        full_range = set() # get all the numbers in the intervals
        for l, r in ranges:
            full_range.update([j for j in range(l, r+1)])
        # check if the given range is a subset of the full range of the given intervals
        return inclusive_range <= full_range