# https://leetcode.com/problems/shuffle-string/description/
# 1528. Shuffle String
class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        """
            instanciate an array of 0 of size len
            then iterate using range(len) over both indices and s
            on the array indices[i] will be the index for s[i]
            join and finish
        """
        res = [0] * len(s)
        for i in range(len(s)):
            idx = indices[i]
            char = s[i]
            # now place on res
            res[idx] = char
        
        return "".join(res)
