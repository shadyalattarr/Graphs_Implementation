from vertex import Vertex


class Edge:
    # pair of vertices
    # weight : int

    def __init__(self, vertex_a: Vertex, vertex_b: Vertex, weight=1):
        self.vertices_pair = (vertex_a, vertex_b)  # using tuples to make pairs
        self.weight = weight

    def __repr__(self):
        return f"{self.vertices_pair} - {self.weight}"
    
    def returnEdge(self):
        return self.vertices_pair[0], self.vertices_pair[1], self.weight 
