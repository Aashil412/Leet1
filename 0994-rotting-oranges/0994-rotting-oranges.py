class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Initialization
        ROWS = len(grid)
        COLS = len(grid[0])
        minutes = -1
        queue = deque()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        FRESH = 0
        # find rotten orange
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                if grid[row][col] == 1:
                    FRESH += 1
        if FRESH == 0:
            return 0
        #bfs
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for x, y in directions:
                    new_row, new_col = r + x, c + y
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
                        FRESH -= 1
                        
    
        if FRESH > 0:
            return -1

        return minutes