# 451. Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/description/
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        # change the word into list for sorting
        word_list = list(s)
        word_list.sort()
        print(word_list)

        word_list.sort(key=lambda x: freq[x], reverse=True)
        print(word_list)

        return "".join(word_list)

soln = Solution()
print(soln.frequencySort("loveleetcode"))