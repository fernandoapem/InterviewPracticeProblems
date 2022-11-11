class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        stack = []
        open = {'(':')', '{':'}','[':']'}
        for x in range(0, len(s)):
            if s[x] in open:
                stack.append(s[x])
            else:
                if len(stack) == 0:
                    return False
                if open[stack.pop()] != s[x]:
                    return False
        if len(stack) > 0:
            return False
        return True
s = "()[]{}"
s2 = "()"
s3 = "(]"
p = Solution()
print(p.isValid(s))
print(p.isValid(s2))
print(p.isValid(s3))
