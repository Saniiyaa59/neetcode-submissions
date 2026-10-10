class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]
        suffix = [1]*len(nums)

        for i in range (1, len(nums)):
            prefix.append(prefix[-1]*nums[i-1])

        for i in range (len(nums)-2, -1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]

        # suffix = suffix[::-1]
        res = []
        for i in range (len(nums)):
            res.append(prefix[i]*suffix[i])
        return res

        