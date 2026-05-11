from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)
        for word in strs:
            arr = [0]*26

            for ch in word:
                index = ord(ch)-97
                arr[index] += 1

            key = str(arr)
            d[key].append(word)

        result = []
        for key in d:
            result.append(d[key])

        return result