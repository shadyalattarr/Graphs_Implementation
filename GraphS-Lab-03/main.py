from vertex import Vertex
from edge import Edge
from Graph import *

v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)

vertex_set = {v1, v2, v3, v4, v5}

edge_set = {
    Edge(v1,v2),
    Edge(v2,v3),
    Edge(v1,v3),
    Edge(v1,v4),
    Edge(v3,v4),
    Edge(v3,v5)
}

g = UndirectedGraph(vertex_set,edge_set)

g.print_adjacency_list()
