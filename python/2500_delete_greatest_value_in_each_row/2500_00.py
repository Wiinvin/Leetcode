class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0

        if len(grid) == 1:
            return sum(grid[0])


        for ni in range(len(grid[0])):
            max_in_cols = []
            for ri in range(len(grid)): 
                maxval = 0
                for ci, idval in enumerate(grid[ri]):
                    if idval >= maxval:
                        maxval = grid[ri][ci]
                        maxvalarg = ci

                max_in_cols.append(grid[ri].pop(maxvalarg))          
            ans += max(max_in_cols)

        return ans
