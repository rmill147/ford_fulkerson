# This class generates a graph given inputs:
# Number of vertices "v", number of source vertices "s", number of sinks "t".
# Output:
# Maximum flow of the graph, potentially the path(s) used.
from random import randint, getrandbits


class GenerateGraph:
    def __init__(self):
        self.edges = list()
        self.V = 0
        self.max_C = 10
        self.source_sink_edges = 1
        self.max_vertices = 4

    # Generate Graph
    def newGraph(self, v, s, t, allow_double_edges=False):
        self.V = v
        edge_list = list()
        m_vertices = v - s - t

        if v > 2:
            # For each vertex
            for ve in range(m_vertices):
                # Random number of edges

                to_nodes = set([randint(0, m_vertices - 1) for _ in range(randint(1, self.max_vertices))])

                # Check for edge to self
                if ve in to_nodes:
                    # If multiple out-edges, remove
                    to_nodes.remove(ve)

                    if len(to_nodes) < 1:
                        if ve < m_vertices - 1:
                            to_nodes.add(ve + 1)
                        else:
                            to_nodes.add(ve - 1)
                if not allow_double_edges:
                    for u in to_nodes.copy():
                        if (u, ve) in edge_list:
                            if getrandbits(1):
                                edge_list.remove((u, ve))
                            else:
                                to_nodes.remove(u)

                [edge_list.append((ve, u)) for u in to_nodes]

        # Source
        for s in range(m_vertices, m_vertices + s):
            to_nodes = set([randint(0, m_vertices - 1) for _ in range(randint(1, self.max_vertices))])
            [edge_list.append((s, u)) for u in to_nodes]

        # Sink
        for t in range(m_vertices + t, v):
            from_nodes = set([randint(0, m_vertices - 1) for _ in range(randint(1, self.max_vertices))])
            [edge_list.append((v, t)) for v in from_nodes]

        # Add in edges for skipped middle vertices:
        in_edges = [u for _, u in edge_list]
        no_in_edges = set(range(m_vertices)) - set(in_edges)
        for ve in no_in_edges:
            u = randint(0, m_vertices - 1)
            if u == ve:
                if u > 0:
                    u -= 1
                else:
                    u += 1
            # if block can cause isolated/dead-end node errors
            if not allow_double_edges:
                if (ve, u) in edge_list:
                    edge_list.remove((ve, u))
            edge_list.append((u, ve))

        # Add weights
        for v, u in edge_list:
            self.edges.append((v, u, randint(1, self.max_C)))
