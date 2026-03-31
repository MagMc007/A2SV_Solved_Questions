# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/?envType=problem-list-v2&envId=backtracking
# 1415. The k-th Lexicographical String of All Happy Strings of Length n
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (2 ** (n-1)):
            return ""
        
        kcnt = 0

        def backtrack(letters):
            nonlocal kcnt

            if len(letters) == n:
                kcnt += 1
                if kcnt == k:
                    return letters
                return

            for i in ['a', 'b', 'c']:
                if letters and letters[-1] == i:
                    continue

                letters.append(i)
                res = backtrack(letters)
                if res:
                    return res
                letters.pop()

        ans = backtrack([])
        return "".join(ans)
'''
time: O(3 ** n)
space: O(n)
'''