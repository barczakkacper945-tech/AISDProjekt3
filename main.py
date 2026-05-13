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
    def tarjan(self):
        marks = {i: "unmarked" for i in range(1, self.nodes + 1)}
        L = []
        has_cycle = False
        def visit(n):
            nonlocal has_cycle
            if marks[n] == "permanent":
                return
            if marks[n] == "temporary":
                has_cycle = True
                return
            marks[n] = "temporary"
            for m in self.adj.get(n, []):
                visit(m)
                if has_cycle:
                    return
            marks[n] = "permanent"
            L.insert(0, n)
        for n in range(1, self.nodes + 1):
            if marks[n] == "unmarked":
                visit(n)
                if has_cycle:
                    break
        if has_cycle:
            print("error (graph has at least one cycle)")
            return None
        return L
def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ["--generate", "--user-provided"]:
        print("Użycie: python main.py [--generate | --user-provided]")
        sys.exit(1)

    mode = sys.argv[1]
    graph = None
    try:
        if mode == "--generate":
            nodes = int(input("nodes> "))
            saturation = float(input("saturation> "))
            graph = Graph(nodes)
            possible_edges = [(i, j) for i in range(1, nodes) for j in range(i + 1, nodes + 1)]
            max_edges = len(possible_edges)
            target_edges = int(max_edges * saturation)
            chosen_edges = random.sample(possible_edges, min(target_edges, max_edges))
            for u, v in chosen_edges:
                graph.add_edge(u, v)
        elif mode == "--user-provided":
            nodes = int(input("nodes> "))
            graph = Graph(nodes)
            print("Wpisz następników oddzielonych spacją, zatwierdź enterem. Pusta linia przechodzi dalej. Ctrl+D (EOF) kończy wczytywanie heredoc.")
            for i in range(1, nodes + 1):
                try:
                    succs = input(f"{i}> ").split()
                    for s in succs:
                        graph.add_edge(i, int(s))
                except EOFError:
                    break
    except ValueError:
        print("Błąd: Oczekiwano wartości liczbowej. Zamykanie programu.")
        sys.exit(1)
    except EOFError:
        print("\nBłąd: Niespodziewany koniec wejścia. Zamykanie programu.")
        sys.exit(1)
    try:
        rep = input("rep (matrix, list, table)> ").strip().lower()
        if rep not in ['matrix', 'list', 'table']:
             print("Nieznana reprezentacja. Ustawiono domyślnie: list")
             rep = 'list'
        while True:
            try:
                action = input("action> ").strip().lower()
            except EOFError:
                break
            if action == "print":
                if rep == "matrix": graph.print_matrix()
                elif rep == "list": graph.print_list()
                elif rep == "table": graph.print_table()
            elif action == "find":
                u = int(input("from> "))
                v = int(input("to> "))
                if graph.find_edge(u, v):
                    print(f"edge ({u},{v}) exists in the Graph")
                else:
                    print(f"edge ({u},{v}) does not exist in the Graph")  
            elif action == "bfs":
                start = int(input("start node> "))
                print(" -> ".join(map(str, graph.bfs(start))))   
            elif action == "dfs":
                start = int(input("start node> "))
                print(" -> ".join(map(str, graph.dfs(start))))  
            elif action == "kahn":
                res = graph.kahn()
                if res: print("Topological sort (Kahn):", res)    
            elif action == "tarjan":
                res = graph.tarjan()
                if res: print("Topological sort (Tarjan):", res)  
            elif action in ["exit", "quit", "q"]:
                break

    except ValueError:
        print("Błąd podanych danych podczas pracy programu. Koniec działania.")
        sys.exit(1)

if __name__ == "__main__":
    main()