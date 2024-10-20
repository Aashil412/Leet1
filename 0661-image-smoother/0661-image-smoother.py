class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(img), len(img[0])

        def calculate_average(row,col):
            top = max(0, row - 1)
            bottom = min(ROWS, row + 2)
            right = min(COLS, col + 2)
            left = max(0, col - 1)
            total = 0
            count = 0
            for r in range(top, bottom):
                for c in range(left, right):
                    total += img[r][c]
                    count += 1
            return total // count

        new_img = [[calculate_average(row,col) for col in range(COLS)] for row in range(ROWS)]
        
        return new_img

        