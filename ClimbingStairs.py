class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for i in range(0,n-1):
            temp = a
            a = a + b
            b = temp
        return a