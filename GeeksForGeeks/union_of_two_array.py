class Solution:    
    def findUnion(self, a, b):
        # code here
        # change to set(keeps elements unique)
        a = set(a)
        b = set(b)
        
        return list(a.union(b))