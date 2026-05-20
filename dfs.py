def dfs(get_neighbors, start, visited=None, result=None):
    if visited is None:
        visited = set()
        result = []
    visited.add(start)
    result.append(start)
    for neighbor in get_neighbors(start):
        if neighbor not in visited:
            dfs(get_neighbors, neighbor, visited, result)
    return result