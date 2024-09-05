class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                count_w = 0
                for u in range(2):
                    for v in range(2):
                        if grid[i + u][j + v] == 'W':
                            count_w += 1
                if count_w != 2:
                    return True
        return False
