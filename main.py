import sys
import random
from graph import Graph
from bfs import bfs
from dfs import dfs
from kahn import kahn
from tarjan import tarjan

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
                print(" -> ".join(map(str, bfs(graph, start))))   
            elif action == "dfs":
                start = int(input("start node> "))
                print(" -> ".join(map(str, dfs(graph, start))))  
            elif action == "kahn":
                res = kahn(graph)
                if res: print("Topological sort (Kahn):", res)    
            elif action == "tarjan":
                res = tarjan(graph)
                if res: print("Topological sort (Tarjan):", res)  
            elif action in ["exit", "quit", "q"]:
                break

    except ValueError:
        print("Błąd podanych danych podczas pracy programu. Koniec działania.")
        sys.exit(1)

if __name__ == "__main__":
    main()