class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def_side = 4
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    ans += def_side

                    if i > 0 and grid[i - 1][j]:
                        ans -= 2

                    if j > 0 and grid[i][j - 1]:
                        ans -= 2

        return ans
