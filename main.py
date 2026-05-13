import sys
import random
from collections import deque

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj = {i: [] for i in range(1, nodes + 1)}
    def add_edge(self, u, v):
        if v not in self.adj[u]:
            self.adj[u].append(v)
            self.adj[u].sort()
    def print_matrix(self):
        matrix = [[0] * self.nodes for _ in range(self.nodes)]
        for u in self.adj:
            for v in self.adj[u]:
                matrix[u-1][v-1] = 1
        print("  " + " ".join(str(i) for i in range(1, self.nodes + 1)))
        print("-" * (self.nodes * 2 + 2))
        for i, row in enumerate(matrix, 1):
            print(f"{i}|" + " ".join(map(str, row)))
    def print_list(self):
        for u in self.adj:
            print(f"{u} -> " + " ".join(map(str, self.adj[u])))
    def print_table(self):
        print("from | to")
        print("---------")
        for u in self.adj:
            for v in self.adj[u]:
                print(f"  {u}  | {v}")
    
    def find_edge(self, u, v):
        return v in self.adj.get(u, [])

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start, visited=None, result=None):
        if visited is None:
            visited = set()
            result = []
        visited.add(start)
        result.append(start)
        for neighbor in self.adj.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited, result)
        return result