import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = defaultdict(int)
        for num in nums:
            d[num]+=1

        q = []

        for key in d:

            hq.heappush(q, [d[key], key])

            if len(q) > k:
                hq.heappop(q)

        result = []

        while q:
            result.append(hq.heappop(q)[1])

        return result



        