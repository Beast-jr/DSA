from math import ceil
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        l,r = 1,max(piles)
        ans=r
        
         
        while l<=r:
            mid=(l+r)//2
            TotalHours=0
            for pile in piles:
                 
                TotalHours+=ceil(pile/mid)
            if  TotalHours<=h:

                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
        