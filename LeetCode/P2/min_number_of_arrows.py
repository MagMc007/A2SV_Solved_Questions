# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
# 452. Minimum Number of Arrows to Burst Balloons
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if len(points) == 1:
            return 1

        points.sort(key=lambda x: x[1])
        arrows = 1

        i = 1
        # print(points)

        prevEnd = points[0][1]

        for start, end in points[1:]:
            if start > prevEnd:
                arrows += 1
                prevEnd = end    
        return arrows
    

soln = Solution()
print(soln.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if len(points) == 1:
            return 1

        points.sort(key=lambda x: x[0])
        arrows = 1

        minPrevend = points[0][1]

        for start, end in points[1:]:
            if start > minPrevend:
                arrows += 1
                minPrevend = end
            minPrevend = min(minPrevend, end)
        
        return arrows