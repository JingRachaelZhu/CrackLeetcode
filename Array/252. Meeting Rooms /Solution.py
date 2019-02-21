# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals:return True    #edge case
        
        intervals =sorted(intervals,key =lambda i:i.start)     #sort 
        former =intervals[0].end
        for i in intervals[1:]:
            if i.start <former:
                return False
            former =i.end
        return True
        