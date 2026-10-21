class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        root = [i for i in range(n+1)]

        def par(x):
            if root[x] == x:
                return x
            return par(root[x])

        for x,y in edges:
            xr, yr = par(x), par(y)
            if xr == yr:
                return [x,y]
            elif x == xr:
                root[x] = yr
            elif y == yr:
                root[y] = xr
            else:
                root[xr] = yr

        
        
            

