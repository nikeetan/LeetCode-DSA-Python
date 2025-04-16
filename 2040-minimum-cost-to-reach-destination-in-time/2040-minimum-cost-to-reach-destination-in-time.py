'''
classic Digiktras
'''
import heapq
from collections import defaultdict
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        '''
        create the adjancency list
        start node is 0
        maintain queue heapq
        every time select the neighbours with minimum time and
        keep a variable to add the cost of passing
        Also every time when we are adding the neighbours will check whether the added time of them will exceeed the max time that is if we come from the node will add time
        But questions there might two pathes
        '''

        # Adjacency matrix
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        # This serves the bidrectional edges
        start_node, destination = 0, len(passingFees) - 1
        
        # Maintain the cost and time array for revisits
        cost_array = [float('inf')] * len(passingFees)
        cost_array[0] = passingFees[0]

        Time = [maxTime + 1] *  len(passingFees)

        Time[0] = 0
        queue = [(passingFees[start_node], 0, 0)]


        # we have to push the neighbors of the 0th node in a heap so that it would be easy for minimal selection

        while queue:
         
            curr_cost, curr_time, node  = heapq.heappop(queue) 
            #print(queue, visited)
            if node == destination:
                return curr_cost
   
            for neighbor in adj.get(node, []):
                nei_node, nei_time = neighbor
            

                if curr_time + nei_time > maxTime:
                    continue
                # new cost and time
                new_cost , new_time = curr_cost + passingFees[nei_node], curr_time + nei_time

                if (new_cost < cost_array[nei_node]) or (new_time  < Time[nei_node]):

                    cost_array[nei_node] = new_cost
                    Time[nei_node] = new_time
                    heappush(queue, (new_cost, new_time , nei_node))
        


        return -1 

        
        #return 0