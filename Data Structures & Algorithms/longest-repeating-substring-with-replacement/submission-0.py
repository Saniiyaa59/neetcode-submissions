class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #idea is to replace less frequent characters with the most frequent one
        arr = [0]*26
        maxLen = 0

        l = 0
        r = 0
        mostFreq = 0

        while r < len(s):

            idx = ord(s[r]) - 65
            arr[idx]+=1
            mostFreq = max(mostFreq, arr[idx])

            while ((r-l+1) - mostFreq) > k:
                i = ord(s[l]) - 65
                arr[i]-=1
                l+=1
                mostFreq = max(arr)

            maxLen = max(maxLen, r-l+1)
            r+=1

        return maxLen



