# https://leetcode.com/problems/fair-distribution-of-cookies/description/
# 2305. Fair Distribution of Cookies
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0] * k
        unfairness = float('inf')

        def backtrack(idx, max_so_far):
            nonlocal unfairness
            
            if idx == len(cookies):
                unfairness = min(unfairness, max(child))
                return 
            
            for i in range(k):
                # prunned
                if max_so_far >= unfairness:
                    return 
                child[i] += cookies[idx]
                backtrack(idx + 1, max(max_so_far, max(child)))
                child[i] -= cookies[idx]

        backtrack(0, 0)
        return unfairness


# time: O(k**n) for each child we are giving each cookie and 
# trying all option exhaustively
# space: O(n+k) => n call stack and k for the children