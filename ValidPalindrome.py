class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = False
        s = s.upper()
        final_str = ""
        for char in s:
            if char.isalnum():
                final_str += char
        if len(s) == 0:
            return True
        length = len(final_str)
        if length % 2 == 0:
            first = final_str[0:int(length/2)]
            second = final_str[int(length/2):length]
            second = second[::-1]
            if first == second:
                check = True
        else:
            first = final_str[0:int(length / 2)]
            second = final_str[int(length / 2) + 1:length]
            second = second[::-1]
            if first == second:
                check = True
        return check
p = Solution()
print(p.isPalindrome("A man, a plan, a canal: Panama"))