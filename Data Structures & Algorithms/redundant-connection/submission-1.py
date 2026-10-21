class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1] * (n + 1)

        # path compression
        def parent(x):
            p = par[x]
            while p != par[p]:
                #path compression
                par[p] = par[par[p]]
                p = par[p]
            return p

        # return if they are false
        def union(n1,n2):
            p1, p2 = parent(n1), parent(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True

        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        

  
        
        
            

