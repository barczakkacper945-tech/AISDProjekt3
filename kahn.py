def kahn(self):
        in_degree = {i: 0 for i in range(1, self.nodes + 1)}
        for u in self.adj:
            for v in self.adj[u]:
                in_degree[v] += 1
        S = [n for n in range(1, self.nodes + 1) if in_degree[n] == 0]
        L = []
        while S:
            n = S.pop(0)
            L.append(n)
            for m in self.adj.get(n, []):
                in_degree[m] -= 1
                if in_degree[m] == 0:
                    S.append(m)
        if len(L) != self.nodes:
            print("error (graph has at least one cycle)")
            return None
        return L