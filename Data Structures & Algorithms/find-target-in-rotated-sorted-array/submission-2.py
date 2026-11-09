class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)-1

        while l <= r:

            mid = (r+l)//2

            if target == nums[mid]:
                return mid

            #left sorted portion
            if nums[l] <= nums[mid]:

                #is target in the left portion?
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1

                else:
                    l = mid + 1

            #right sorted portion
            elif nums[mid] <= nums[r]:

                #is target in the right portion?
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1

                else:
                    r = mid - 1

        return -1
