# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
# 84. Largest Rectangle in Histogram
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int: 
        max_area = 0
        n = len(heights)

        stack = []  # monotonically increasing stack: format [span, elemt]

        for i in range(n):
            starts = i

            while stack and stack[-1][1] > heights[i]:
                idx, top = stack.pop()
                max_area = max(max_area, top * (i - idx))
                starts = idx
            
            stack.append([starts, heights[i]])
        
        # for what ever is left in stack
        while stack:
            idx, top = stack.pop()
            max_area = max(max_area, top * (n - idx))
            # print(idx, top)

        return max_area

print(Solution().largestRectangleArea([2,1,5,6,2,3]))