class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        #One pass
        total =0
        tank =0
        start =0
        for i in range(len(gas)):
            cur =gas[i]-cost[i]
            tank +=cur
            total +=cur
            if  tank <0:
                start =i+1
                tank =0

        if total <0:
            return -1:
        else:
            return start
        #Two pass
        #determine if have a solution
        if sum(gas)<sum(cost):
            return -1

        #find the start station
        tank =0
        start =0
        for i in range(len(gas)):
            cur =gas[i]-cost[i]
            tank +=cur              #update tank
            if tank <0:
                start =i+1          #if A cant reach B,then any station bwt A and B cant reach B,either.
                tank =0
        return start