from collections import Counter
import heapq as hq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = Counter(nums)
        q = []

        for key in d:
            hq.heappush(q, [d.get(key), key])
            if len(q) > k:
                hq.heappop(q)

        result = []
        while k > 0 and q:
            result.append(hq.heappop(q)[1])
        return result
        