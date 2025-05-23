# A graph is a valid tree when we have no cycles in it how do we detect the cycle is dfs or bfs having the visit node and c

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = defaultdict(list)
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def dfs(node):
            stk = []
            stk.append(node)
            visited.add(node)
            while stk:
                curr_node = stk.pop()
                for nei in adj.get(curr_node, []):
                    if nei not in visited:
                        visited.add(nei)
                        stk.append(nei)
        dfs(0)
        return len(visited) == n

        
        # visited = [False] * n
        # stk = []
        # visited[0] = True
        # stk.append(0)
        
        # while stk:
        #     node = stk.pop()
        #     for nei in adj.get(node, []):
        #         if not (visited[nei]):
        #             visited[nei] = True
        #             stk.append(nei)
        # return all(visited)
        
