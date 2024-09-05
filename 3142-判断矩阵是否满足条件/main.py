class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i + 1 < len(grid):
                    if grid[i][j] != grid[i + 1][j]:
                        return False
                if j + 1 < len(grid[i]):
                    if grid[i][j] == grid[i][j + 1]:
                        return False
        return True
