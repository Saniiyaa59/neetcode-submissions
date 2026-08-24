from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        cycle = set()
        visit = set()
        result = []

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        def dfs(curr):

            if curr in cycle:
                return []

            if curr in visit:
                return result

            cycle.add(curr)
            for pre in adj[curr]:
                if not dfs(pre):
                    return []

            cycle.remove(curr)
            visit.add(curr)
            result.append(curr)

            return result

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return result


            

        