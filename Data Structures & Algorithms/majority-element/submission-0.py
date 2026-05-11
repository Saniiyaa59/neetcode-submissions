class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums.sort()
        l = 0
        r = 0

        while r < len(nums):

            if nums[l] != nums[r]:
                l = r

            if r-l+1 > len(nums)//2:
                return nums[l]

            r+=1

        return nums[0]

            

            


        
            