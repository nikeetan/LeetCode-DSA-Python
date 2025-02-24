def dfs(visited,graph,start):
    if start not in visited:
        visited.append(start)
    if start in graph:
        node=start
        for i in range(len(graph[node])):
            if graph[node][i] in visited:
                continue
            else:
                start= graph[node][i]
                dfs(visited,graph,start)
        return visited
graph={
    'A':['B','C'],
    'B':'D',
    'C':'D'
}
start='A'
visited=[]
print(dfs(visited,graph,start))