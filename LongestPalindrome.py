from typing import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = Counter(s)
        counter = 0
        check = False
        if len(letters) == 1:
            return letters[list(letters.keys())[0]]
        for char in letters:
            if letters[char] != 1:
                counter = counter + ( letters[char] - (letters[char]%2))
            elif letters[char] == 1 and check is False:
                counter = counter + 1
                check = True
        return counter
p = Solution()
print(p.longestPalindrome("abccccdd"))
print(p.longestPalindrome("ccc"))
print(p.longestPalindrome("aA"))
print(p.longestPalindrome("bananas"))
print(5 % 2)
print(11 % 2)
print(3 % 2)