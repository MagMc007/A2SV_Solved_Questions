# https://leetcode.com/problems/score-of-parentheses/description/?envType=problem-list-v2&envId=stack
# 856. Score of Parentheses
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        stack = []

        for i in s:
            if i != ")":
                stack.append(i)
            else:
                between = 0

                while stack[-1] != "(":
                    between += int(stack.pop())
                
                # pop the last (
                stack.pop()

                if not between: # was just ()
                    between = 1
                
                if stack:  # was nested
                    stack.append(between * 2)
                else:
                    score += between
                
        return score

print(Solution().scoreOfParentheses("((())())"))

# time: O(n)
# space: O(n)
                