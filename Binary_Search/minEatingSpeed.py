import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        while l < r:
            mid = (l + r) // 2
            
            hours_needed = 0
            for p in piles:
                hours_needed += (p + mid - 1) // mid 
            
            if hours_needed > h:
                l = mid + 1
            else:
                r = mid
                
        
        return l
