class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        root = [i for i in range(n+1)]
        rank = [1] * (n + 1)


        # path compression
        def par(x):
            if root[x] != x:
                root[x] = par(root[x])
            return root[x]

        for x,y in edges:
            xr, yr = par(x), par(y)
            if xr == yr:
                return [x,y]

            if rank[xr] < rank[yr]:
                root[xr] = root[yr]
                rank[yr] += rank[xr]
            else:
                root[yr] = root[xr]
                rank[xr] += rank[yr]
        
            # elif x == xr:
            #     root[x] = yr
            # elif y == yr:
            #     root[y] = xr
            # else:
            #     root[xr] = yr

        
        
            


