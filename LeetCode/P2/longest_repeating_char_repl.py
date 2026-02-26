# https://leetcode.com/problems/longest-repeating-character-replacement/description/
# 424. Longest Repeating Character Replacement
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # dynamic sliding window
        # variables to track maximum repeated elem in 
        # a window
        leng = 0
        
        hash = Counter()

        left = 0

        for right in range(len(s)):
            # insert the right one
            hash[s[right]] += 1

            # get the elemt with max_cnt
            curr_max = 0
            for key, val in hash.items(): # max of 26 times # still linear
                curr_max = max(curr_max, val)

            size = right - left + 1

            # can i do switching
            if size - curr_max <= k:
                leng = max(leng, size)
                continue

            while size - curr_max > k:
                hash[s[left]] -= 1
                left += 1
                size -= 1

        return leng

                
soln = Solution()
print(soln.characterReplacement(s = "ABAB", k = 2))

# time: O(26 * n) => O(n)
# space: O(26) => on the hash map
#               so it beccomes O(1)