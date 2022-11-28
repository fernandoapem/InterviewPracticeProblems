from typing import Counter
class Solution:
    def canConstruct(self,ransomNote: str, magazine: str ) -> bool:
        t = {}
        for char in magazine:
            if char not in t:
                t[char] = 1
            else:
                t[char] = t[char]+1
        for char in ransomNote:
            if char not in t:
                return False
            else:
                t[char] = t[char]-1
        check = True
        for x in t:
            if t[x] < 0 and x in ransomNote:
                check = False
        return check
p = Solution()
print(p.canConstruct("aa","ab"))