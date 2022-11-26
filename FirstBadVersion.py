class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        
        while low < high:
            mid = int((low+high)/2)
            if isBadVersion(mid) == True: ##API Defined in problem
                high = mid
            else:
                low = mid + 1
        return high