from typing import List
from typing import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = Counter(nums)
        for number in n:
            if n[number] > int(len(nums)/2):
                return number
    def majorityElement2(self, nums:List[int]) -> int:
        map = {}
        for number in nums:
            if number not in map:
                map[number] = 1
            else:
                map[number] = map[number] + 1
        for number in map:
            if map[number] > int(len(nums)/2):
                return number
        return -1
    def majorityElement3(self, nums:List[int]) -> int: # Boyer-Moore Voting Algorithm
        result = count = 0
        for n in nums:
            if count == 0:
                result = n
            count += (1 if n == result else -1)
        return result 
p = Solution()
print(p.majorityElement2([2,2,1,1,1,2,2]))