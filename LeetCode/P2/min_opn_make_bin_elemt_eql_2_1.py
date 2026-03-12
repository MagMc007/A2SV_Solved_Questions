# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/?envType=problem-list-v2&envId=queue
#3191. Minimum Operations to Make Binary Array Elements Equal to One I
from collections import deque

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # deque of size 3 before processing at all times
        flips = 0
        
        q = deque()

        for i in nums:
            q.append(i)

            if len(q) == 3:
                if q[0] == 0:
                    # now we flip the 3
                    flips += 1
                    for j in range(3):
                        if q[j] == 1:
                            q[j] = 0
                        else:
                            q[j] = 1
            print(q)
            # remove all ones
            while q and q[0] == 1:
                q.popleft()

        # q must be empty at the end
        if not q:
            return flips

        return -1

# space: O(3) => O(1) on q only
# time: O(n) # 


# more optimization: remove the queue and process
# elements directly