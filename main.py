import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# get info from  csv
data = pd.read_csv('signalData - Sheet2.csv')
node_id = data['Signal ID'].tolist()
node_id = [x for x in node_id if str(x) != 'nan']
print("Number of nodes: ", len(node_id))
print("Node IDs: ", node_id)

edges = data['Edges'].tolist()

volumes = data['Avg daily volume'].tolist()
print("Volumes: ", volumes)

tuples = []
i = 0
for x in edges:
    tokens = x.strip('[]').split(',')
    vol = int(volumes[i])
    tokens_x = int(tokens[0])
    tokens_y = int(tokens[1])
    tuples.append((tokens_x, tokens_y, vol))

    # Missing Data
    if tokens_x not in node_id:
        node_id.append(tokens_x)
    if tokens_y not in node_id:
        node_id.append(tokens_y)
    i += 1

print("edges: ", tuples)

# Make the graph
graph = nx.DiGraph()
# graph.add_nodes_from(node_id)
graph.add_weighted_edges_from(tuples)
pos = nx.random_layout(graph)
nx.draw(graph, with_labels=True, pos=pos, node_size=200, alpha=0.8, font_weight="bold", arrows=True)
plt.show()

# Implement FF
source = 1414
sink = 6235


# Implement BFS for source s and sink t to make sure there is a clear path
# s - source, t - sink, g - graph <nx.DiGraph>, nodes - node_id's
def ek_solve(source, sink, graph, nodes):
    # Parent holds all nodes
    parent = [-1] * len(node_id)
    max_flow = 0

    # Each loop, evaluates if there exists an unvisited path from s to t
    path_exists = bfs(int(source), int(sink), graph, node_id, parent)

    # Build residual edges
    for u, v, _ in tuples:
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

        path_exists = bfs(int(source), int(sink), graph, node_id, parent)

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


max_flow = ek_solve(int(source), int(sink), graph, node_id)
print(f"Maximum flow is {max_flow} vehicles")
