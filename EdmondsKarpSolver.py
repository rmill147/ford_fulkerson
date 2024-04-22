def ek_solve(source, sink, graph, nodes):
    # Parent holds all nodes
    parent = [-1] * len(nodes)
    max_flow = 0

    # Each loop, evaluates if there exists an unvisited path from s to t
    path_exists = bfs(int(source), int(sink), graph, nodes, parent)

    # Build residual edges
    for u, v in list(graph.edges).copy():
        graph.add_edge(v, u, weight=0)

    while path_exists:
        path_flow = float("Inf")
        s = sink
        while s != source:
            # parent[s] - gets parent node in active path of current sink
            # graph[parent[s]] - gets parent node edges
            # graph[parent[s]][s] - gets weight of current sink from parent's edges
            parent_vertex = parent[nodes.index(s)]
            path_flow = min(path_flow, graph.edges[parent_vertex, s]['weight'])
            s = parent_vertex

        max_flow += path_flow

        # Get new residual graph
        v = sink
        while v != source:
            u = parent[nodes.index(v)]
            # Subract flow from current edge
            graph.edges[u, v]['weight'] -= path_flow
            graph.edges[v, u]['weight'] += path_flow

            v = parent[nodes.index(v)]

        path_exists = bfs(int(source), int(sink), graph, nodes, parent)

    return max_flow


def bfs(s, t, g, nodes, parent):
    visited = [False] * len(nodes)
    # print("visited")
    # print(visited)
    queue = [s]
    index = nodes.index(s)
    visited[index] = True
    # print(visited)

    while queue:
        # print(f"queue: {queue}")
        # Dequeue a vertex from queue and print it
        popped = queue.pop()
        print(f"Popped {popped}")
        # Need children of popped node
        # Get all neighbors of the dequeued vertex u
        # If adjacent has not been visited, then mark it visited and enqueue it
        for vertex_id, vertex_dest, data in g.out_edges(popped, data=True):
            # print(f"val: {val}")
            ind = nodes.index(vertex_dest)
            # print(f"ind: {ind}")
            val = data['weight']
            if not visited[ind] and val > 0:
                queue.append(vertex_dest)
                visited[ind] = True
                parent[ind] = vertex_id
                if vertex_dest == t:
                    return True

        # if we didn't reach sink in BFS starting from source, return false
    return False
