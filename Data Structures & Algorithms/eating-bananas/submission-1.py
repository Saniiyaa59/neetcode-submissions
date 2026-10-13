import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_k = max(piles)

        def time_taken(curr_k):
            time = 0
            for p in piles:
                time += math.ceil(p/curr_k)
            return time

        l = 1
        r = max_k
        res = max_k

        while l <= r:

            m = (l+r)//2

            time = time_taken(m)

            if(time > h):
                l = m+1

            elif(time <= h):
                res = min(res, m)
                r = m-1

        return res

