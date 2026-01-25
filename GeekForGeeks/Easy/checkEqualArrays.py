from collections import Counter

class Solution:
    def checkEqual(self, a, b) -> bool:
        if Counter(a) == Counter(b):
            return True
        return False
