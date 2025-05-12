"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    '''
    treating as graph
    '''
    def __init__(self):
        self.visited = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        # if visited return the same node
        if head in self.visited:
            return self.visited[head]

        # create a new node if its not visited
        new_node = Node(head.val, None, None)

        self.visited[head] = new_node

        # One DFS for next pointer
        new_node.next = self.copyRandomList(head.next)
        # One DFS for the random pointer
        new_node.random = self.copyRandomList(head.random)
    
        return new_node


