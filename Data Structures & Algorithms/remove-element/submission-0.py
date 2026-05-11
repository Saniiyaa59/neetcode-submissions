class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        #move the pointer if it is val 
        #if the current is not val -> swap

        l = 0
        r = 0

        while r < len(nums):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
            r+=1

        return l
