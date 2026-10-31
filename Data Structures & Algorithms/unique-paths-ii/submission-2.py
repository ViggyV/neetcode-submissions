class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        M, N = len(obstacleGrid), len(obstacleGrid[0])   
        prevRow = [0] * (N + 1)
        prevRow[N - 1] = 1

        for r in range(M-1, -1, -1):
            for c in range(N-1, -1, -1):
                if obstacleGrid[r][c]:
                    prevRow[c] = 0
                else:
                    prevRow[c] = prevRow[c] + prevRow[c+1]
        return prevRow[0]
        