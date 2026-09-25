
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for i in range (len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = len(nums)-1
            prev = float('inf')

            while(j < k):

                if prev == nums[j]:
                    j+=1
                    continue

                sums = nums[i] + nums[j] + nums[k]

                if sums < 0:
                    j+=1
                
                elif sums > 0:
                    k-=1

                else:
                    result.append([nums[i], nums[j], nums[k]])
                    prev = nums[j]
                    j+=1
                    k-=1

        return result




        



