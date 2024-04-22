# This class generates a graph given inputs:
# Number of vertices "v", number of source vertices "s", number of sinks "t".
# Output:
# Maximum flow of the graph, potentially the path(s) used.
from math import isqrt
from random import randint

class GenerateGraph:
    def __init__(self):
        self.edges = list()
        self.V = 0
        self.max_C = 10
        self.source_sink_edges = 1

    # Generate Graph
    def newGraph(self, v, s, t):
        self.V = v
        m_vertices = v - s - t

        if v > 2:
            # For each vertex
            for ve in range(m_vertices):
                # Random number of edges
                to_nodes = set([randint(0, m_vertices-1) for _ in range(randint(1, m_vertices))])

                if ve in to_nodes:
                    # If multiple out-edges, remove
                    if len(to_nodes) > 1:
                        to_nodes.remove(ve)
                    # Else add another
                    else:
                        if ve < m_vertices-1:
                            to_nodes.add(ve+1)
                        else:
                            to_nodes.add(ve-1)
                [self.edges.append((ve, u, randint(1, self.max_C))) for u in to_nodes]

        # Source
        for s in range(m_vertices, m_vertices + s):
            to_nodes = set([randint(0, m_vertices - 1) for _ in range(randint(1, v//2+1))])
            [self.edges.append((s, u, randint(1, self.max_C))) for u in to_nodes]

        # Sink
        for t in range(m_vertices + t, v):
            from_nodes = set([randint(0, m_vertices - 1) for _ in range(randint(1, v // 2 + 1))])
            [self.edges.append((v, t, randint(1, self.max_C))) for v in from_nodes]

        # Add in edges for skipped middle vertices:
        in_edges = [u for _, u, _ in self.edges]
        no_in_edges = set(range(m_vertices)) - set(in_edges)
        for ve in no_in_edges:
            u = randint(0, m_vertices-1)
            if u == ve:
                if u > 0:
                    u -= 1
                else:
                    u += 1
            self.edges.append((u, ve, randint(1, self.max_C)))


