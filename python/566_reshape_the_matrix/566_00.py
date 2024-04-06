
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rr = len(mat)
        cc = len(mat[0])

        if rr*cc != r*c:
            return mat

        ans = [[0] * c for i in range(r)]
        
        rri = -1
        cci = 0
        for ri in range(r):
            for ci in range(c):
                if cci % cc == 0:
                    rri += 1
                    cci = 0

                ans[ri][ci] = mat[rri][cci]
                cci += 1

        return ans
