class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        creating the edge list
        '''        
        edges = []
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            for j in range(min_len):
                if word1[j] != word2[j]:
                    edges.append([word1[j], word2[j]])
                    break
            else:
                if len(word1) > len(word2):
                    return ""  # Invalid order


        # Classic topological sort
        adj = defaultdict(list)
        indegree = defaultdict(int)
        unique_chars = set(''.join(words))
        for char in unique_chars:
            indegree[char] = 0

        for u , v in edges:
            adj[u].append(v)
            indegree[v] += 1
       
        queue = deque()
        for key, val in indegree.items():
            if val == 0:
                queue.append(key)
        print(queue)
        
        visited = []
        while queue:
            node = queue.popleft()
            visited.append(node)
            for nei in adj.get(node, []):
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        if len(visited) < len(unique_chars):
            return ""  
        return ''.join(visited)