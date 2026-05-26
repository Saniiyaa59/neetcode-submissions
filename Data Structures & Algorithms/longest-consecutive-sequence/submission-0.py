from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        maxLen = 0

        for num in numSet:
            #smallest no. in sequence
            if num-1 not in numSet: 
                length = 1
                x = num
                while x + 1 in numSet:
                    length+=1
                    x+=1
                maxLen = max(maxLen, length)

        return maxLen


