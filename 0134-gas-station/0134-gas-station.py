class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        requiredCost = sum(cost)
        availableGas = sum(gas)

        #Base condition
        if availableGas < requiredCost:
            return -1
        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i] 
            if tank < 0:
                start = (i + 1)
                tank = 0
        return start
    
        



        
        
