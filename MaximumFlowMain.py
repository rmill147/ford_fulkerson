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
# Double edges, an edge from (u, v) and (v, u) breaks current graph implementation edmonds-karp
allow_double_edges = False

random_graph = GenerateGraph()
random_graph.newGraph(num_vertices, num_source, num_sink, allow_double_edges)

graph_edges = random_graph.edges

source = 8
sink = 9
nodes = range(num_vertices)

# Random Graph Alternative = nx.erdos_renyi_graph()
graph = nx.DiGraph()
graph.add_weighted_edges_from(graph_edges)
# pos = nx.random_layout(graph)
# pos = nx.spring_layout(graph)
# Spiral seems to work the best for visuals:
pos = nx.spiral_layout(graph)

weights = nx.get_edge_attributes(graph, 'weight')

bidirect_edges = [edge for edge in graph.edges if reversed(edge) in graph.edges]
straight_edges = set(graph.edges) - set(bidirect_edges)

bidirect_edge_labels = {}
for v, u in bidirect_edges:
    bidirect_edge_labels[(v, u)] = graph.get_edge_data(v, u)['weight']

straight_edge_labels = {}
for v, u in straight_edges:
    straight_edge_labels[(v, u)] = graph.get_edge_data(v, u)['weight']


nx.draw(graph, pos=pos, node_size=200, alpha=0.8)
nx.draw_networkx_labels(graph, pos=pos, font_weight="bold")
nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=bidirect_edge_labels, label_pos=.8, font_size=8)
nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=straight_edge_labels, font_size=8)

'''
nx.draw_networkx_nodes(graph, pos=pos, node_size=200, alpha=0.8)
nx.draw_networkx_labels(graph, pos=pos, font_weight="bold")
nx.draw_networkx_edges(graph, pos=pos, edgelist=straight_edges)
nx.draw_networkx_edges(graph, pos=pos, edgelist=bidirect_edges, connectionstyle='arc3,rad=.1')
nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=nx.get_edge_attributes(graph, 'weight'), font_size=8)
'''

max_flow = EdmondsKarpSolver.ek_solve(int(source), int(sink), graph, nodes)
print(f"Maximum flow is {max_flow}")

plt.show()