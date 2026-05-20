def tarjan(nodes, get_neighbors):
    marks = {i: "unmarked" for i in range(1, nodes + 1)}
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
        for m in get_neighbors(n):
            visit(m)
            if has_cycle:
                return
        marks[n] = "permanent"
        L.insert(0, n)
        
    for n in range(1, nodes + 1):
        if marks[n] == "unmarked":
            visit(n)
            if has_cycle:
                break
    if has_cycle:
        print("error (graph has at least one cycle)")
        return None
    return L