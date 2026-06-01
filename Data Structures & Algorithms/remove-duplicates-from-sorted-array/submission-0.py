class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = 0
        r = 0
        prev = nums[0]

        while r < len(nums):

            if prev != nums[r]:
                prev = nums[r]
                nums[l+1], nums[r] = nums[r], nums[l+1]
                l+=1

            r+=1

        return l+1