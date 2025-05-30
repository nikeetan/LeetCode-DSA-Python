'''
use khans algorithm and create the order and once you have the indices
'''

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build the graph
        adj = {}
        indegree = [0] * numCourses
        for prev, next in prerequisites:
            if next not in adj:
                adj[next] = [prev]
            else:
                adj[next].append(prev)
        prereq_map = {}
        res = []
        def dfs(crs):
            if crs not in prereq_map:
                prereq_map[crs] = set()
                for nei in adj.get(crs, []):
                    prereq_map[crs] |= dfs(nei)
                prereq_map[crs].add(crs)                
            return prereq_map[crs]
        
        for crs in range(numCourses):
            dfs(crs)

        for u, v in queries:
            res.append(u in prereq_map[v])
        return res

       
        # res = []
        # for nodes in queries:
        #     flag = 0
        #     dest, start = nodes
        #     queue = deque([start])
        #     while queue:
        #         curr_node = queue.popleft()
        #         if curr_node == dest:
        #             flag = 1
        #             res.append(True)
        #             break
        #         for nei in adj.get(curr_node, []):
        #             queue.append(nei)
        #     if flag == 0:
        #         res.append(False)
        # return res

