def dfs(graph, start, visited=None, result=None):
        if visited is None:
            visited = set()
            result = []
        visited.add(start)
        result.append(start)
        for neighbor in graph.adj.get(start, []):
            if neighbor not in visited:
                dfs(graph, neighbor, visited, result)
        return result