import re

class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        adj = defaultdict(list)
        raw_map = {}
        indegree = defaultdict(int)
        for symbol, literal in replacements:
            raw_map[symbol] = literal
            for match in re.findall(r"%([A-Z]+)%", literal) :
                adj[match].append(symbol)
                indegree [symbol] += 1
        
        queue = deque()
        
        for symbol in raw_map:
            if indegree[symbol] == 0:
                queue.append(symbol)
        
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)  
            for neighbor in adj.get(node, []):
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        resolved_map = {}

        for symbol in topo_order:
            raw_value = raw_map[symbol]
            i = 0
            result = ''
            while i < len(raw_value):
                if raw_value[i] == '%':
                    j = i + 1
                    placeholder = ""
                    while j < len(raw_value) and raw_value[j] != '%':
                        placeholder += raw_value[j]
                        j += 1 
                    i = j + 1
                    result += resolved_map.get(placeholder, f"%{placeholder}%")
                else:
                    result += raw_value[i]
                    i += 1
            resolved_map[symbol] = result

        i = 0
        final_result = ""

        while i < len(text):
            if text[i] == '%':
                j = i + 1
                placeholder = ""
                while j < len(text) and text[j] != '%':
                    placeholder += text[j]
                    j += 1
                i = j + 1  # move past second '%'
                final_result += resolved_map.get(placeholder, f"%{placeholder}%")
            else:
                final_result += text[i]
                i += 1
        return final_result

                    

