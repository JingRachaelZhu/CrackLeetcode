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
        #Chronological Ordering
    
        if not intervals:return 0
        
        start =[]
        end =[]
        for i in intervals:         #take start and end time individualy
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        room =0
        index_e =0
        for index_s in range(len(start)):      
            if start[index_s] <end[index_e]:  #It means start before end,need a room
                room +=1
            else:
                index_e +=1                   #It means start after free a room.
                
        return room
