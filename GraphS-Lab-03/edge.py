from vertex import Vertex


class Edge:
    # pair of vertices
    # weight : int

    def __init__(self, vertex_a: Vertex, vertex_b: Vertex, weight=1):
        self.vertices_pair = (vertex_a, vertex_b)  # using tuples to make pairs
        self.weight = weight
