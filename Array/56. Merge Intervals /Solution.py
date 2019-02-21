# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals :return []
        
        intervals =sorted(intervals,key =lambda i:i.start)   #the key point : use lambda funtion
        res =[intervals[0]]
        for i in intervals[1:]:
            if i.start <=res[-1].end:                        #compare the start with previous end
                res[-1].end =max(res[-1].end,i.end)
            else:
                res +=[i]
                
        return res