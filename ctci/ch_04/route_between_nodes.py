
from __future__ import annotations
from typing import List, Tuple, Dict
from collections import deque

class GraphNode:

    def __init__(self, val, neighbors: List[GraphNode] = None):
        self.value = val
        if not neighbors:
            self.neighbors = []
        else:
            self.neighbors = neighbors
    
    def __str__(self):
        return f"{[self.value]!r} -> {[neigbhor.value for neigbhor in self.neighbors]}"
    
class Graph:

    def __init__(self, nodes: Dict[int, GraphNode]):
        self.nodes = nodes

    @classmethod
    def generate_graph(cls, data: List[Tuple[int, List]]):
        nodes = {val: GraphNode(val) for val, _ in data}
        # print(nodes)

        for val, neighbors in data:
            node = nodes[val]
            node.neighbors.extend(nodes[neighbor_val] for neighbor_val in neighbors)
        
        return cls(nodes)

    def __str__(self):
        return '\n'.join(str(node) for node in self.nodes.values())


def has_route(g: Graph, start, end):
    visited = set()
    nodes = deque()
    nodes.append(g.nodes[start])
    while nodes:
        node = nodes.popleft()
        if node.value == end:
            return True
        visited.add(node.value)
        nodes.extend(neighbor for neighbor in node.neighbors if neighbor.value not in visited)
    return False


test_case = [
    (1, [2,3]),
    (2, [3]),
    (3, [5]),
    (4, [3]),
    (5, [7, 4]),
    (7, []),
    (8, [])
]

graph = Graph.generate_graph(test_case)
print(graph)
print(has_route(graph, 1, 7))
print(has_route(graph, 1, 8))