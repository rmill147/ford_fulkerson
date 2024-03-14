import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


# get info from  csv
data = pd.read_csv('signalData - Sheet2.csv')
num_nodes = len(data)
print("Number of nodes: ", num_nodes)
node_id = data['Signal ID'].tolist()
node_id = [x for x in node_id if str(x) != 'nan']
print("Node IDs: ", node_id)

edges = data['Edges'].tolist()

volumes = data['Avg daily volume'].tolist()
print("Volumes: ", volumes)

tuples = []
i = 0
for x in edges:
    tokens = x.strip('[]').split(',')
    vol = volumes[i]
    vol = int(vol)
    tokens_x = int(tokens[0])
    tokens_y = int(tokens[1])
    tuples.append((tokens_x, tokens_y, vol))
    i = i + 1
print("edges: ", tuples)

# Make the graph
graph = nx.DiGraph()
graph.add_nodes_from(node_id)
graph.add_weighted_edges_from(tuples)
pos = nx.random_layout(graph)
nx.draw(graph, with_labels=True, pos=pos, node_size=200, alpha=0.8, font_weight="bold", arrows=True)
plt.show()

# Implement FF
source = node_id[0]
sink = 6235

# Implement BFS for source s and sink t to make sure there is a clear path
def bfs(s, t, g, nodes):
    parent =  []
    visited = [False] * (len(node_id))
    print("visited")
    print(visited)
    queue = []
    queue.append(s)
    index = nodes.index(s)
    visited[index] = True
    print(visited)

    while queue:
        print(f"queue: {queue}")
        # Dequeue a vertex from queue and print it
        popped = queue.pop(0)
        print(f"Popped {popped}")
        neighbors_iter = nx.neighbors(g,popped)
        neighbors =  []
        print("neighbors")
        for x in neighbors_iter:
            print(x)
            neighbors.append(x)

        # Get all neighbors of the dequeued vertex u
        # If adjacent has not been visited, then mark it visited and enqueue it
        for val in nodes:
            print(f"val: {val}")
            ind = nodes.index(val)
            print(f"ind: {ind}")
            if visited[ind] == False and val > 0:
                queue.append(val)
                visited[ind] = True
                parent.append(val)
                if ind == t:
                    return True, parent

        # if we didn't reach sink in BFS starting from source, return false
    return False, parent


parent = bfs(int(source), int(sink), graph, node_id)



