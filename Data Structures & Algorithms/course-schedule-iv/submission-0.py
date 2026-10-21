class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)

        for prereq, crs in prerequisites:
            adj[crs].append(prereq)

        preMap = {}

        def dfs(crs):
            if crs in preMap:
                return preMap[crs]
            preMap[crs] = set()
            for prereq in adj[crs]:
                preMap[crs] |= dfs(prereq) # union
            preMap[crs].add(crs)
            return preMap[crs]

        
        for crs in range(numCourses):
            dfs(crs)

        res = []

        for u,v in queries:
            res.append(u in preMap[v])
        return res