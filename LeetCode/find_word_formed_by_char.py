# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
# 1160. Find Words That Can Be Formed by Characters
from collections import Counter
import copy


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        hash = Counter(chars)

        length = 0
        for word in words:
            deepcopy = copy.deepcopy(hash)
            # using the deep copy we may perform
            # decrement
            is_good = True
            for char in word:
                if deepcopy.get(char):
                    # the char is in the deepcop
                    if deepcopy[char] > 0:
                        deepcopy[char] -= 1
                    else:
                        is_good = False
                        break
                else:
                    is_good = False
                    break
            if is_good:
                length += len(word)
        return length

soln = Solution()
print(soln.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))


            
