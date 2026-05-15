class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        suffix = []

        prod = 1
        for i in range (len(nums)):
            prefix.append(prod)
            prod *= nums[i]

        prod = 1
        for i in range (len(nums)-1,-1,-1):
            suffix.append(prod)
            prod *= nums[i]

        suffix = suffix[::-1]
        result = []
        for i in range (len(prefix)):
            result.append(prefix[i]*suffix[i])
        return result


