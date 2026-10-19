class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs from each chest
        # keep track of distance
        # update all INFs to the distance when processing neighbors
        # only add as neighbor if not -1 or 0 (land = INF)
        INF = 2147483647
        queue = deque()
        ROWS,COLS = len(grid),len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i,j))
        distance = 1
        while queue:
            for i in range(len(queue)):
                cx, cy = queue.popleft()
                neighbors = [(cx+dx,cy+dy) for dx,dy in ((0,-1), (0,1), (-1,0), (1,0)) if 0 <= cx+dx < ROWS and 0 <= cy+dy < COLS and grid[cx+dx][cy+dy] == INF]
                for nx,ny in neighbors:
                    grid[nx][ny] = distance
                    queue.append((nx,ny))
            distance += 1
        
