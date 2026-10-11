class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []


        for ch in operations:
            if ch == "+":
                scores.append(scores[-1] + scores[-2])
            elif ch == "D":
                scores.append(scores[-1] * 2)
            elif ch == "C":
                scores.pop()
            else:
                scores.append(int(ch))
        
        return sum(scores)