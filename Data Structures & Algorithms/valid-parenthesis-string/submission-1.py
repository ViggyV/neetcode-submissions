class Solution:
    def checkValidString(self, s: str) -> bool:
        
        dict = {")": "("}
        
        stack = []
        star = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == "*":
                star.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while stack and star:
            if stack.pop() > star.pop():
                return False
        
        return not stack
            
