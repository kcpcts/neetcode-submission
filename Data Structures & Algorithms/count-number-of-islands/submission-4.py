class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs and set to 0 when we see a 1

        def bfs(sr,sc):
            queue = deque()
            queue.append((sr,sc))
            grid[sr][sc] = '0'
            
            while queue:
                cx, cy = queue.popleft()
    
      
                neighbors = [(cx+dx,cy+dy) for dy,dx in ((0,1), (1,0), (0,-1), (-1,0)) if 0 <= cx+dx < ROWS and 0 <= cy+dy < COLS and grid[cx+dx][cy+dy] == '1']
                for n in neighbors:
                    queue.append(n)
                    grid[n[0]][n[1]] = '0'
            
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    bfs(i,j)
                    count += 1
        return count

