class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        nums.sort()
        l = 0
        r = 0
        res = set()
        n = len(nums)

        while(r < n):
            
            if nums[r] != nums[l]:
                l = r            

            if r-l+1 > n//3:
                res.add(nums[l])

            r+=1

        return list(res)


        