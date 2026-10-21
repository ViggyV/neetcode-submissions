class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        sys.setrecursionlimit(500 * 500 + 1000)
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        ROWS, COLS = len(grid1), len(grid1[0])
        count = 0

        visit = set()

        def dfs(r,c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid2[r][c] == 0 or (r,c) in visit):
                    return True

            visit.add((r,c))
            res = True
            if grid1[r][c] == 0:
                res = False

            for dr, dc in directions:
                res = dfs(dr + r, dc + c) and res 

            return res


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid2[r][c] and dfs(r,c):
                    count += 1

        return count