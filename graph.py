class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.raw_edges = []
        self.matrix = None
        self.adjacency_list = None
        self.edge_table = None
        self.rep_type = None

    def add_edge(self, u, v):
        if (u, v) not in self.raw_edges:
            self.raw_edges.append((u, v))
            self.raw_edges.sort()

    def set_representation(self, rep_type):
        self.rep_type = rep_type
        if rep_type == "matrix":
            self.matrix = [[0] * self.nodes for _ in range(self.nodes)]
            for u, v in self.raw_edges:
                self.matrix[u-1][v-1] = 1
        elif rep_type == "list":
            self.adjacency_list = {i: [] for i in range(1, self.nodes + 1)}
            for u, v in self.raw_edges:
                self.adjacency_list[u].append(v)
            for i in self.adjacency_list:
                self.adjacency_list[i].sort()
        elif rep_type == "table":
            self.edge_table = list(self.raw_edges)

    def get_neighbors(self, node):
        if self.rep_type == "matrix":
            neighbors = []
            for v_idx in range(self.nodes):
                if self.matrix[node-1][v_idx] == 1:
                    neighbors.append(v_idx + 1)
            return neighbors
            
        elif self.rep_type == "list":
            return self.adjacency_list.get(node, [])
            
        elif self.rep_type == "table":
            neighbors = []
            for u, v in self.edge_table:
                if u == node:
                    neighbors.append(v)
            return neighbors
        return []

    def find_edge(self, u, v):
        if self.rep_type == "matrix":
            if 1 <= u <= self.nodes and 1 <= v <= self.nodes:
                return self.matrix[u-1][v-1] == 1
            return False
        elif self.rep_type == "list":
            return v in self.adjacency_list.get(u, [])
        elif self.rep_type == "table":
            for edge_u, edge_v in self.edge_table:
                if edge_u == u and edge_v == v:
                    return True
            return False
        return False

    def print_matrix(self):
        mat = self.matrix if self.matrix is not None else [[0] * self.nodes for _ in range(self.nodes)]
        if self.matrix is None:
            for u, v in self.raw_edges: mat[u-1][v-1] = 1
        print("  " + " ".join(str(i) for i in range(1, self.nodes + 1)))
        print("-" * (self.nodes * 2 + 2))
        for i, row in enumerate(mat, 1):
            print(f"{i}|" + " ".join(map(str, row)))

    def print_list(self):
        lst = self.adjacency_list
        if lst is None:
            lst = {i: [] for i in range(1, self.nodes + 1)}
            for u, v in self.raw_edges: lst[u].append(v)
            for i in lst: lst[i].sort()
        for u in lst:
            print(f"{u} -> " + " ".join(map(str, lst[u])))

    def print_table(self):
        tbl = self.edge_table if self.edge_table is not None else self.raw_edges
        print("from | to")
        print("---------")
        for u, v in tbl:
            print(f"  {u}  | {v}")