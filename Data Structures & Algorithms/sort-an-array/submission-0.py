class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        #merge sort

        def mergeSort(left, right):

            if left >= right:
                return [nums[right]]

            mid = (right+left)//2
            leftSorted = mergeSort(left, mid)
            rightSorted = mergeSort(mid+1, right)

            p1 = 0
            p2 = 0

            res = []

            while p1 < len(leftSorted) and p2 < len(rightSorted):

                if leftSorted[p1] < rightSorted[p2]:
                    res.append(leftSorted[p1])
                    p1+=1
                else:
                    res.append(rightSorted[p2])
                    p2+=1

            if p1 < len(leftSorted):
                res += leftSorted[p1:]
            
            if p2 < len(rightSorted):
                res += rightSorted[p2:]

            return res

        return mergeSort(0, len(nums)-1)
