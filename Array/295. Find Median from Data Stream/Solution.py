from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small =[]              #maxheap for smaller helf
        self.large =[]              #minheap for larger half
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small) ==len(self.large):
            heapq.heappush(self.large,-heapq.heappushpop(self.small,-num))          
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large,num))      ##take the oppositive num into smallheap
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) ==len(self.large):
            return float(self.large[0] -self.small[0])/2.0
        else:
            return float(self.large[0])
 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()