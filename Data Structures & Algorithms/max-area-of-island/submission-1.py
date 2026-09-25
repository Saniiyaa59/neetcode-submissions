class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visit = set()
        dirn = [[-1,0], [1,0], [0,-1], [0,1]]
        m = len(grid)
        n = len(grid[0])

        def bfs(i,j):

            q = collections.deque()
            area = 1
            q.append((i,j))
            visit.add((i,j))

            while q:

                x, y = q.popleft()

                for dx, dy in dirn:

                    x_ = x + dx
                    y_ = y + dy

                    if(x_ < 0 or x_ >= m or y_ < 0 or y_ >= n or grid[x_][y_] == 0 or (x_, y_) in visit):
                        continue

                    visit.add((x_, y_))
                    q.append((x_, y_))
                    area+=1

            return area

        
        max_area = 0
        for i in range (m):
            for j in range (n):
                if grid[i][j] == 1 and (i, j) not in visit:
                    max_area = max(max_area, bfs(i,j))

        return max_area