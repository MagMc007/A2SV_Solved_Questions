# https://leetcode.com/problems/open-the-lock/description/
# 752. Open the Lock
from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:  
        deadends = set(deadends)  # make lookup O(1)

        if "0000" in deadends:
            return -1

        visited = set()
        q = deque([((0, 0, 0, 0), 0)]) # the combination and the cnt: state
        
        def toStr(li):
            li = list(map(str, li))
            return "".join(li)

        while q:
            combination = q.popleft()
            cnt = combination[1]


            if toStr(combination[0]) == target: # 0000
                return cnt
            
            cnt += 1

            # now the current combo can go in 2 ways 
            for i in range(4):
                # at each step we alter one of the 4 circles
                # 1. add one to it
                toadd = list(combination[0])
                tosub = list(combination[0])

                if toadd[i] == 9:
                    toadd[i] = 0
                else:
                    toadd[i] += 1
                
                # parse to tuple and append
                tupCombo = tuple(toadd)

                if tupCombo not in visited and toStr(tupCombo) not in deadends:
                    if toStr(tupCombo) == target:
                        return cnt
                    
                    q.append((tupCombo, cnt))
                    visited.add(tupCombo)
                
                # 2. subtract one
                
                if tosub[i] == 0:
                    tosub[i] = 9
                else:
                    tosub[i] -= 1
                
                # parse to tuple and append
                tupCombo = tuple(tosub)
                if tupCombo not in visited and toStr(tupCombo) not in deadends:
                    if toStr(tupCombo) == target:
                        return cnt
                    
                    q.append((tupCombo, cnt))
                    visited.add(tupCombo)
                    
        # un reachable
        return -1