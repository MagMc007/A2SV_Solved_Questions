# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/description/
# 1247. Minimum Swaps to Make Strings Equal

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # possible combinations are 
        # xy and yx across the 2 strings

        xy, yx = 0, 0
        
        i = 0

        while i < len(s1):
            # xy
            if s1[i] == "x" and s2[i] == "y":
                xy += 1
            
            # yx
            if s2[i] == "x" and s1[i] == "y":
                yx += 1

            i += 1
        
        # both need to be even so that the pairing could work
        if (xy + yx) % 2 != 0:
            return -1

        # for xy we need xy//2 swaps
        # for yx we also need yx//2 swaps
        # cosider the fact that both may be odd
        odd_catcher = 2 if xy % 2 else 0
        return xy // 2 + yx // 2 + odd_catcher
    
