# MaximumFlowMain - Driver file
# Generates random graph/list of edges using GenerateGraph
# Solves Using EK_Solve

from GenerateGraph import GenerateGraph
import EdmondsKarpSolver
import networkx as nx
import matplotlib.pyplot as plt


# import pandas as pd

num_vertices = 10
num_source = 1
num_sink = 1

random_graph = GenerateGraph()
random_graph.newGraph(num_vertices, num_source, num_sink)

graph_edges = random_graph.edges

print(graph_edges)

graph = nx.DiGraph()
graph.add_weighted_edges_from(graph_edges)
pos = nx.random_layout(graph)
nx.draw(graph, with_labels=True, pos=pos, node_size=200, alpha=0.8, font_weight="bold", arrows=True)
plt.show()

source = 8
sink = 9
nodes = range(num_vertices)

print(graph.edges)

max_flow = EdmondsKarpSolver.ek_solve(int(source), int(sink), graph, nodes)
print(f"Maximum flow is {max_flow}")