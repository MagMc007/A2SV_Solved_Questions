# https://leetcode.com/problems/remove-invalid-parentheses/description/
# 301. Remove Invalid Parentheses
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Step 1: count invalid parentheses
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1

        res = set()

        def dfs(i, l, r, open_cnt, path):
            if i == len(s):
                if l == 0 and r == 0 and open_cnt == 0:
                    res.add(path)
                return

            c = s[i]

            # REMOVE
            if c == '(' and l > 0:
                dfs(i+1, l-1, r, open_cnt, path)
            elif c == ')' and r > 0:
                dfs(i+1, l, r-1, open_cnt, path)

            # KEEP
            if c == '(':
                dfs(i+1, l, r, open_cnt+1, path + c)
            elif c == ')':
                if open_cnt > 0:
                    dfs(i+1, l, r, open_cnt-1, path + c)
            else:
                dfs(i+1, l, r, open_cnt, path + c)

        dfs(0, l, r, 0, "")
        return list(res)