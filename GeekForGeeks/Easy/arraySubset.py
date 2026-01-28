#User function Template for python3
from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        a_count = Counter(a)
        b_count = Counter(b)
        hash_a = set(a)
        
        
        for num in b:
            if num not in hash_a:
                return False
            elif a_count[num] < b_count[num]:
                return False
                
        return True
    
    
    
