# https://leetcode.com/problems/group-anagrams/
# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the key must be the words arranged in an order
        # split to list and concatenate

        hash = {}

        for word in strs:
            word_sorted = "".join(sorted(word))

            if word_sorted in hash:
                hash[word_sorted].append(word)
            else:
                hash[word_sorted] = [word]
        return list(hash.values())