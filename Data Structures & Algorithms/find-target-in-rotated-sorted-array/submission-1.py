class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1

        while l <= r:

            m = (l+r)//2

            #found if mid is target
            if nums[m] == target:
                return m

            #if left portion is sorted
            if nums[l] <= nums[m]:
                
                #target is in left portion
                if target < nums[m] and target >= nums[l]:
                    r = m-1
                
                else:
                    l = m+1

            #right portion is sorted
            else:
                #target is in right portion
                if target > nums[m] and target <= nums[r]:
                    l = m+1
                
                else:
                    r = m-1

        return -1


                
