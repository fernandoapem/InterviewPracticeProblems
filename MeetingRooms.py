from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        result = {}
        for x in intervals:
            result[x[0]] = x[1]
        for x in result:
            for y in range(0,len(intervals)):
                if ((x in range(intervals[y][0],intervals[y][1]+1)) or (result[x] in range(intervals[y][0],intervals[y][1]+1))) and ([x,result[x]]!=[intervals[y][0],intervals[y][1]]):
                    return False
        return True
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for x in range(0,len(intervals)-1):
            if intervals[x][1] > intervals[x+1][0]:
                return False
        return True

p = Solution()
#print(1 in range(0,4))
print(p.canAttendMeetings([[7,10],[2,4]]))
print(p.canAttendMeetings([[0,30],[5,10],[15,20]]))