class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        M, N = len(grid), len(grid[0])

        res = [[float("inf")] * (N + 1) for r in range(M + 1)]
        res[M][N - 1] = 0

        for r in range(M - 1, -1, -1):
            for c in range(N -1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r+1][c], res[r][c+1])
        
        return res[0][0]
