def kahn(nodes, get_neighbors):
    in_degree = {i: 0 for i in range(1, nodes + 1)}
    for u in range(1, nodes + 1):
        for v in get_neighbors(u):
            in_degree[v] += 1
            
    S = [n for n in range(1, nodes + 1) if in_degree[n] == 0]
    L = []
    while S:
        n = S.pop(0)
        L.append(n)
        for m in get_neighbors(n):
            in_degree[m] -= 1
            if in_degree[m] == 0:
                S.append(m)
    if len(L) != nodes:
        print("error (graph has at least one cycle)")
        return None
    return L