from vertex import Vertex
from edge import Edge
from minheap import MinHeap
from graph import *

v0 = Vertex(0)
v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)
v6 = Vertex(6)
v7 = Vertex(7)

vertex_set = {v0, v1, v2, v3, v4, v5, v6, v7}

edge_set = {
    Edge(v0, v1, 9),
    Edge(v0, v2, 2),
    Edge(v1, v3, 7),
    Edge(v2, v4, 1),
    Edge(v2, v5, 4),
    Edge(v2, v6, 5),
    Edge(v1, v6, 9),
    Edge(v4, v7, 4),
    Edge(v5, v7, 6),
    Edge(v2, v6, 5)

}

g = UndirectedGraph(vertex_set, edge_set)

g.print_adjacency_list()

mst = g.prim_MST(v2)
print("------")
mst.print_adjacency_list()
print("ex2")

v_set2 = {v0, v1, v2, v3, v4}
e_set2 = {
    Edge(v0, v1, 2),
    Edge(v0, v3, 6),
    Edge(v1, v3, 8),
    Edge(v1, v2, 3),
    Edge(v1, v4, 5),
    Edge(v2, v4, 7),
    Edge(v3, v4, 9),
}
g2 = UndirectedGraph(v_set2, e_set2)

g2.print_adjacency_list()

mst2 = g2.prim_MST(v0)
print("------")
mst2.print_adjacency_list()