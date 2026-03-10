# https://leetcode.com/problems/crawler-log-folder/description/
# 1598. Crawler Log Folder
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # ../ - pop
        # ./ - pass
        # x/ - push

        stack = 0

        for i in logs:
            if i == "./":
                continue

            if i == "../":
                if stack:
                    stack -= 1
            else:
                stack += 1

        return stack
    
# time- O(n)
# space- O(1) || if it was stack it would have been O(n)