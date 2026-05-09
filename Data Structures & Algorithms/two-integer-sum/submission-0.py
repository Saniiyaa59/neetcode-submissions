class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index_map = {}

        for i in range (len(nums)):
            index_map[nums[i]] = i

        for i in range (len(nums)):

            curr = nums[i]
            if target - curr in index_map and index_map[target-curr] != i:
                return [i, index_map[target-curr]]
                
        return []
