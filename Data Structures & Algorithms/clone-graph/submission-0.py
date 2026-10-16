"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def df(node):
            if visited.get(node) is None:
                newNode = Node(node.val)
                visited[node] = newNode
                newNode.neighbors = [df(nb) for nb in node.neighbors]
            
            return visited.get(node)
        
        if node is None:
            return None
        return df(node)
                
            
        