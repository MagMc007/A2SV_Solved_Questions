#User function Template for python3
from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        # use a counter dictionary on b
        b = Counter(b)
        
        # get elemt from a, find it in dict and then decrease value to deal with repeated vals
        for elmt in a:
            if b.get(elmt):
                b[elmt] -= 1
                if b[elmt] == 0:
                    b.pop(elmt) # remove the elmt if all have been seen 
        return not b
        
    
    
    
    
