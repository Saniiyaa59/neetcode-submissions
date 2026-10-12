class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums)-1
        res = nums[0]

        while(l <= r):

            mid = (l+r)//2
            res = min(res, nums[mid])

            if(nums[l] <= nums[mid]):
                res = min(res, nums[l])
                l = mid+1

            elif(nums[mid] < nums[r]):
                r = mid-1

        return res

            
        