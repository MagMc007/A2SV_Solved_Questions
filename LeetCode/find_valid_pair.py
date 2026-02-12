# https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/description/
# 3438. Find Valid Pair of Adjacent Digits in Stringf
from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        cnt = Counter(s)

        for i in range(len(s) - 1):
            cnt_num_1 = cnt[s[i]]
            cnt_num_2 = cnt[s[i+1]]
            first_num = int(s[i])
            second_num = int(s[i+1])

            if cnt_num_1 == first_num and cnt_num_2 == second_num:
                if first_num != second_num:
                    return f"{first_num}{second_num}"
        return ""