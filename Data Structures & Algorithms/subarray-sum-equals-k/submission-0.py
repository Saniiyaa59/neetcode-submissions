from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #The question is: "What previous prefix sum do I need to subtract (not add) from my current sum to get k?"
        
        sums = 0
        seen = defaultdict(int)
        seen[0] = 1
        result = 0

        for num in nums:
            sums += num
            if sums - k in seen:
                result += seen[sums - k]
            seen[sums] +=1

        return result

