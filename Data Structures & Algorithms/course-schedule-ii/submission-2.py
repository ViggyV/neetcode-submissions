class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)


        # course 3 states
        # visited - > add to ouput
        # visiting -> crs not added to ouput but in cycle
        # unvisit -> neither

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for dep in preMap[crs]:
                if not dfs(dep):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return []

        
        return output