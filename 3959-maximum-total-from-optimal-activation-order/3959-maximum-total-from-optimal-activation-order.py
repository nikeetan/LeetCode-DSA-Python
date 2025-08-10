'''
To activate an inactive element at index i, the number of currently active elements must be strictly less than limit[i].

'''

import heapq
class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        
        totalActivation = 0
        #Start with the least limit value element
        elementQueue = []
        activeElements = []
        for i in range(len(value)):
            heapq.heappush(elementQueue, (limit[i], -value[i]))
        
        currActive = 0
        while elementQueue:
            lt, val = heapq.heappop(elementQueue)
            if len(activeElements) >= lt:
                continue
            
            heapq.heappush(activeElements, lt)
            totalActivation +=  (-1 * val)
            currActive = len(activeElements)
            
            while activeElements and activeElements[0] <= currActive:
                heapq.heappop(activeElements)

            while elementQueue and elementQueue[0][0] <= currActive:
                heapq.heappop(elementQueue)
     
    
        return totalActivation

            
