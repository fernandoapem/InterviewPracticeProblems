from typing import List
class Solution:
    def BinarySearch(self, nums: List[int], target: int) -> int:
        result = -1
        if target not in nums:
            return -1
        result = self.recursiveSearch(0,len(nums)-1,target)
        return result
    def recursiveSearch(self,nums: List[int],start: int, end: int,target: int) -> int:
        x = int((start + end ) / 2)
        if nums[x] == target:
            return x
        elif nums[x] > target:
            return self.recursiveSearch(nums,start,x-1,target)
        elif nums[x] < target:
            return self.recursiveSearch(nums,x+1,end,target)
        
p = Solution()
nums = [-1,0,3,5,9,12]
print(p.BinarySearch(nums,9))
print(p.BinarySearch(nums,2))