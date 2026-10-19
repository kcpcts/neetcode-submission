class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        # bfs flood fill from each rotten orange
        # find all starting positions (2s)
        # expand only to 1s, mark them as 2s

        starts = []
        left = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    starts.append((i,j))
                if grid[i][j] == 1:
                    left += 1

        
        queue = deque(starts)
        time = 0
        while queue:
            if left > 0:
                time += 1
            for i in range(len(queue)):
                cx,cy = queue.popleft()
                neighbors = [(cx+dx, cy+dy) for dx,dy in ((0,1), (1,0), (-1,0), (0,-1)) if 0 <= cx+dx < ROWS and 0 <= cy+dy < COLS and grid[cx+dx][cy+dy] == 1]
                for nx,ny in neighbors:
                    grid[nx][ny] = 2
                    left -= 1
                    queue.append((nx,ny))
            
            
        # if there are any 1s left then its not achievable so return -1
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        return time

        