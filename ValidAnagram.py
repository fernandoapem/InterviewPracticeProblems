class Solution:
    #First Solution
    def isAnagram(self, s: str, t: str) -> bool:
        check = True
        letters = {}
        if len(s) != len(t):
            return False
        for char in s:
                letters[char] = 0
        for char in s:
                x = letters[char] + 1
                letters[char] = x
        for char in t:
                if char not in s:
                    return False
                if t.count(char) != letters[char]:
                    check = False
        return check
    #Too Optimal
    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(t) == sorted(s)

    def isAnagram3(self, s: str, t: str) -> bool:
        letters = {}
        for char in s:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
        for char in t:
            if char not in letters:
                return False
            else:
                letters[char] -= 1
        for char in letters:
            if letters[char] != 0:
                return False
        return True

p = Solution()
print(p.isAnagram3("anagram","nagaram"))
