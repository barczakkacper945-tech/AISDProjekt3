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