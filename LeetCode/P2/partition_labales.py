# https://leetcode.com/problems/partition-labels/description/
# 763. Partition 
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # get the ending idx for every element in s
        hash = {}

        for idx, ch in enumerate(s):
            hash[ch] = idx
        
        # keep track of the size and the maximum end idx for repeated
        # elemts

        size = 0
        end = 0
        i = 0

        output = []

        while i < len(s):
            # record size of a grp and start a new group
            if i > end:
                output.append(size)
                end = hash[s[i]]
                size = 0
            else:
                end = max(end, hash[s[i]])

            size += 1
            i += 1

        # whether it is a single elmt or group the last is skipped
        # a condition of append accounts for those > len
        output.append(size)
        return output


soln = Solution()
print(soln.partitionLabels(s="eccbbbbdec"))


"""
    Time => O(n) as we go through the elements 1 times
    space => on the dictionary hash the keys are unique and we only have 
            26 letters so it is O(1)
"""