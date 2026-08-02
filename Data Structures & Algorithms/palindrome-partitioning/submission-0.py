class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []

        def backtrack(i):
            if i >= len(s):
                res.append(sub.copy())
                return 
            
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    sub.append(s[i:j+1])
                    backtrack(j+1)
                    sub.pop()

        backtrack(0)

        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True