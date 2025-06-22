'''
i am thinking of applying bfs and also having max_prov as varialble
'''
from collections import defaultdict
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        # bellman ford
        price = [float('-inf')] * n
        price[start_node] = 1
       
        for i in range(n - 1):
            temp = price.copy()
            flag = 0
            for i in range(len(edges)):
                u, v = edges[i]
                prob = succProb[i]
                #print(u, v, prob)
                if price[u] != float('-inf') and price[u] *  prob > price[v]:
                    temp[v] = price[u] * prob
                    flag = 1
                elif price[v] != float('-inf') and price[v] * prob > price[u]:
                    temp[u] = price[v] * prob
                    flag = 1
            if flag == 0:
                break
            price = temp.copy()
        return price[end_node] if price[end_node] != float('-inf') else 0 







        '''
        # build graph
        adj = defaultdict(list)
        succ_prob_map = {}
        for i in range(len(edges)):
            u, v = edges[i]
            if (u, v) not in succ_prob_map:
                succ_prob_map[(u, v)] = succProb[i]
                succ_prob_map[(v, u)] = succProb[i]
            adj[u].append(v)
            adj[v].append(u)
    
        # initialize the queue
        queue = deque()
        queue.append((start_node, 1))
        
        # will have the seen set
        seen = set()
        seen.add(start_node)
        # Probablity
        max_prob = 0.0
        #traverse
        while queue:
            curr_node, curr_prob = queue.popleft()
            if curr_node == end_node:
                max_prob = max(max_prob, curr_prob)
                continue

            for nei in adj.get(curr_node, []):
                if (curr_node, nei) not in seen:
                    seen.add((curr_node, nei))
                    queue.append((nei, curr_prob * succ_prob_map[(curr_node, nei)]))

        return max_prob
        '''
