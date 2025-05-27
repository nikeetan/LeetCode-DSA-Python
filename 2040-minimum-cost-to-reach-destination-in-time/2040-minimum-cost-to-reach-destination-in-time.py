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
        # Create Graph
        adj = collections.defaultdict(list)
        for u, v , time in edges:
            adj[u].append((v, time))
            adj[v].append((u, time))

        nodes_num = len(passingFees)
        # Two arrays to maintain the cost and time of traversal
        cost = [float('inf') for _ in range(nodes_num)]
        time = [maxTime for _ in range(nodes_num)]
        # Start point heap = (cost, time , node)
        start  = (passingFees[0], 0, 0)
        queue = []
        heapq.heappush(queue, start)
        
        while queue:
            curr_cost, curr_time, curr_node = heappop(queue)
            if curr_node == nodes_num - 1:
                return curr_cost
            
            for nei_info in adj.get(curr_node, []):
                nei_node, nei_time = nei_info
                if curr_time + nei_time > maxTime:
                    continue

                # if we find a cheaper way to reach next city then only we will explore
                if (curr_cost + passingFees[nei_node] < cost[nei_node]) or (curr_time + nei_time < time[nei_node]):
                    cost[nei_node] = curr_cost + passingFees[nei_node]             
                    time[nei_node] = curr_time + nei_time
                
                    heappush(queue, (cost[nei_node], time[nei_node], nei_node))

        return -1