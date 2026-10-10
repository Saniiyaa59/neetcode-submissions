class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [[temperatures[0],0]]
        result = [0]*len(temperatures)

        for i in range (1, len(temperatures)):

            while stack and temperatures[i] > stack[-1][0]:
                temp, index = stack.pop()
                result[index] = i - index
            stack.append([temperatures[i], i])
        return result


