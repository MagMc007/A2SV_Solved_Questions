# https://leetcode.com/problems/word-break-ii/description/?envType=problem-list-v2&envId=backtracking
# 140. Word Break II

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            result = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in word_set:
                    for suffix in backtrack(end):
                        if suffix:
                            result.append(word + " " + suffix)
                        else:
                            result.append(word)

            memo[start] = result
            return result

        return backtrack(0)