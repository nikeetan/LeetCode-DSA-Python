'''
DSU
and check whether the terminal nodes are connected to the every neighbor of the current node
'''
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # reverse graph
        adj = {}
        n = len(graph)
        indegree = [0] * n
        for curr_node in range(n):
            for nei in graph[curr_node]:
                if nei not in adj:
                    adj[nei] = [curr_node]
                else:
                    adj[nei].append(curr_node)
                indegree[curr_node] += 1
        # Intialize the terminal nodes that is starting from terminal 
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        # bfs
        # from terminal we are moving to safe node and from safe node to another likewise
        safe_nodes = [False] * n
        visited = set()
        while queue:
            node = queue.popleft()
            safe_nodes[node] = True
            visited.add(node)
            for nei in adj.get(node, []):
                if nei not in visited:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
        res_nodes = []
        for i in range(n):
            if safe_nodes[i]:
                res_nodes.append(i)
        return res_nodes
        

            
        
