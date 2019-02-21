# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        #PriorityQueues_minheap优先队列
        
        import heapq
        if not intervals:return 0
        
        res =1
        intervals =sorted(intervals,key=lambda i:i.start)
        heap =[intervals[0].end]
        for n in intervals[1:]:        
            if n.start <heap[0]:          #If start before end,add room
                res +=1
                heapq.heappush(heap,n.end)    
            else:
                heapq.heapreplace(heap,n.end)      #It means release a room for this start,
        
        return res