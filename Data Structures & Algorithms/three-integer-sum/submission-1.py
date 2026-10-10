class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range (len(nums)):

            if(i > 0 and nums[i] == nums[i-1]):
                continue

            prev = float('inf')
            l = i+1
            r = len(nums)-1

            while l < r:

                if prev == nums[l]:
                    l+=1
                    continue

                sums = nums[i]+nums[l]+nums[r]

                if sums < 0:
                    l+=1

                elif sums > 0:
                    r-=1

                else:
                    res.append([nums[i],nums[l],nums[r]])
                    prev = nums[l]
                    l+=1
                    r-=1

        return res

