# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# 17. Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        ans = []

        def backtrack(idx, letters):
            # base case
            if len(letters) == len(digits):
                ans.append("".join(letters))
                return

            for i in hash[digits[idx]]:
                letters.append(i)
                backtrack(idx+1, letters)
                letters.pop()
            
        backtrack(0, [])
        return ans

'''
time: O(n * 4**n) # n for join and the other for the tree
space: O(n * 4 ** n) # n for the string lenght and 4 ** n being the maximum count 
        we may have
'''