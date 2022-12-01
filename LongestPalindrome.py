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
    def longestPalindrome2(self, s: str) -> int:
        letters = Counter(s)
        check = 0
        result = 0
        for count in letters.values:
            if count % 2 == 0:
                result = result + count
            else:
                odd = 1
                result = result + count - 1
        return result + odd
        
p = Solution()
print(p.longestPalindrome("abccccdd"))
print(p.longestPalindrome("ccc"))
print(p.longestPalindrome("aA"))
print(p.longestPalindrome("bananas"))