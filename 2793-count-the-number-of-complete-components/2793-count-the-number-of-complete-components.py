from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        first i need to think of keeping track of vertices pattern 
        '''
        #Creating a dictionary to hold the vertices
        #Intitializing the graph

        vertices_counter = defaultdict(int)
        graph = [[] for _ in range(n)]

        # Intitalizing the self loops
        for vertex in range(n):
            graph[vertex] = [vertex]
        
        # Appending edges now

        for edge,vertice in edges:
            graph[edge].append(vertice)
            graph[vertice].append(edge)

        for i in graph:

            neighbours = tuple(sorted(i))
            vertices_counter[neighbours] += 1
        
        count_neighbours = 0
        for neighbours, freq in vertices_counter.items():
            if len(neighbours) == freq:
                count_neighbours += 1
        return count_neighbours
