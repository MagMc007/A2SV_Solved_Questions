# https://leetcode.com/problems/removing-stars-from-a-string/description/
# 2390. Removing Stars From a String
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in s:
            if stack and i == "*":
                stack.pop()
            else:
                stack.append(i)
            
        return "".join(stack)