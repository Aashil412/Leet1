class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # do bfs
        # see if its one turn to 0 and add 1 to adjacent 
        ROWS = len(isWater)
        COLS = len(isWater[0])

        results = [[-1 for _ in range(COLS)] for _ in range(ROWS)]
        queue = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if isWater[row][col] == 1:
                    queue.append((row,col))
                    results[row][col] = 0
        
        while queue:
            row_idx, col_idx = queue.popleft()
            for row, col in [(row_idx + 1, col_idx),(row_idx - 1, col_idx),(row_idx,col_idx + 1),(row_idx,col_idx-1)]:
                if 0 <= row < ROWS and 0 <= col < COLS and results[row][col] == -1:
                    results[row][col] = 1 + results[row_idx][col_idx] 
                    queue.append((row,col))

        return results
