from collections import Counter
class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        a = Counter(a)
        b = Counter(b)
        
        return a == b
        