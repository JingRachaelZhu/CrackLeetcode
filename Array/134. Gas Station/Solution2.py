class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start =len(gas)-1			#start starts from the end,end starts from the head
        end =0						#to avoid some adge cases(eg.starting station at 0)
        tank =gas[start]-cost[start]
        while start >end:
        	if tank >=0:
        		tank +=gas[end]-cost[end]
        		end +=1
        	else:
        		start -=1
        		tank +=gas[start]-cost[start]

        if tank >=0:
        	return start
        else:
        	return -1
