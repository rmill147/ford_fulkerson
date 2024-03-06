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
    print("vol: ", vol)
    vol = int(vol)
    tokens_x = int(tokens[0])
    tokens_y = int(tokens[1])
    tuples.append((tokens_x, tokens_y, vol))
    i = i + 1
print("edges: ", tuples)

# Make the graph
G = nx.DiGraph()
G.add_nodes_from(node_id)
G.add_weighted_edges_from(tuples)
pos = nx.random_layout(G)
nx.draw(G, with_labels=True, pos=pos, node_size=200, alpha=0.8, font_weight="bold", arrows=True)
plt.show()

