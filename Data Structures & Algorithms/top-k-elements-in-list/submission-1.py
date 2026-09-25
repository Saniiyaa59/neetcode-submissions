import heapq as hq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        q = []
        d = defaultdict(int)

        for num in nums:
            d[num]+=1

        for key in d:
            hq.heappush(q, [d[key], key])

            if len(q) > k:
                hq.heappop(q)


        result = []
        while q:
            result.append(hq.heappop(q)[1])

        return result
        
            
        
