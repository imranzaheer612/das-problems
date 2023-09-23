class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        # binary search the row num
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0 , ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][-1] < target :
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot): 
            return False

        # binary search the target in row
        l, r = 0 , COLS - 1
        row = (top + bot) // 2
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
            
        return False
    

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 13

# matrix = [[1],[3]]
# target = 3

sol = Solution()
print(sol.searchMatrix(matrix, target))