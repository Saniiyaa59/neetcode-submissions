from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        indegree = [0]*numCourses
        result = []

        for crs, pre in prerequisites:
            indegree[pre]+=1
            adj[crs].append(pre)

        q = []
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
                result.append(crs)

        while q:

            curr = q.pop(0)

            for pre in adj[curr]:
                indegree[pre]-=1
                if indegree[pre] == 0:
                    q.append(pre)
                    result.append(pre)

        return result[::-1] if len(result) == numCourses else []




        
        