class Solution:
    def isPalindrome(self, s: str) -> bool:
        end = len(s) - 1
        beg = 0

        while(beg < end):
            while beg < end and not s[beg].isalnum():
                beg += 1
            while beg < end and not s[end].isalnum():
                end -= 1
            if s[beg].lower() != s[end].lower():
                return False
            beg += 1
            end -= 1
        return True