class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        r = 0
        sums = 0
        minLen = float('inf')

        while r < len(nums):
            sums += nums[r]

            while sums >= target:
                minLen = min(minLen, r-l+1)
                sums -= nums[l]
                l+=1

            r+=1
        
        return minLen if minLen != float('inf') else 0

