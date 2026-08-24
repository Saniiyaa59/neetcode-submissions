from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        cycle = set()
        visit = set()

        for pre, course in prerequisites:
            adj[pre].append(course)

        def dfs(curr):

            if curr in cycle:
                return False

            if curr in visit:
                return True
            
            cycle.add(curr)
            for pre in adj[curr]:
                if(not dfs(pre)):
                    return False
            cycle.remove(curr)
            visit.add(curr)
            
            return True

        for crs in range(numCourses):
            if (not dfs(crs)):
                return False
        return True

