from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for num in nums:
            if num not in result:
                result[num] = 1
            else:
                result[num] += 1
        for x in result:
            if result[x] >= 2:
                return True
        return False
    def containsDuplicate2(self, nums: List[int]) -> bool:
        nums.sort()
        for x in range(0,len(nums)):
            if x < len(nums)-1:
                if nums[x] == nums[x+1]:
                    return True
        return False