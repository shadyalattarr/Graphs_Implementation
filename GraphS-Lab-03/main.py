from vertex import Vertex
from edge import Edge
from minheap import MinHeap
from graph import *

# v0 = Vertex(0)
# v1 = Vertex(1)
# v2 = Vertex(2)
# v3 = Vertex(3)
# v4 = Vertex(4)
# v5 = Vertex(5)
# v6 = Vertex(6)
# v7 = Vertex(7)

# vertex_set = {v0, v1, v2, v3, v4, v5, v6, v7}

# edge_set = {
#     Edge(v0, v1, 9),
#     Edge(v0, v2, 2),
#     Edge(v1, v3, 7),
#     Edge(v2, v4, 1),
#     Edge(v2, v5, 4),
#     Edge(v2, v6, 5),
#     Edge(v1, v6, 9),
#     Edge(v4, v7, 4),
#     Edge(v5, v7, 6),
#     Edge(v2, v6, 5)

# }

# g = UndirectedGraph(vertex_set, edge_set)

# g.print_adjacency_list()

# mst = g.prim_MST(v2)
# print("------")
# mst.print_adjacency_list()
# print("ex2")

# v0 = Vertex(0)
# v1 = Vertex(1)
# v2 = Vertex(2)
# v3 = Vertex(3)
# v4 = Vertex(4)
# v5 = Vertex(5)
# v6 = Vertex(6)
# v7 = Vertex(7)
# v8 = Vertex(8)

# vertex_set = {v0, v1, v2, v3, v4, v5, v6, v7, v8}

# edge_set = {
#     Edge(v0, v1, 4),
#     Edge(v0, v7, 8),
#     Edge(v1, v7, 11),
#     Edge(v1, v2, 8),
#     Edge(v7, v8, 7),
#     Edge(v7, v6,1),
#     Edge(v2, v8, 2),
#     Edge(v8, v6, 6),
#     Edge(v2, v3, 7),
#     Edge(v2, v5, 4),
#     Edge(v6, v5, 2),
#     Edge(v3, v5, 14),
#     Edge(v3, v4, 9),
#     Edge(v5, v4, 10)
# }
# g2 = UndirectedGraph(vertex_set, edge_set)
# mst = g2.Kruskal_MST()
# print("------")
# mst.print_adjacency_list()
# print("ex3")
# print("------")
# dict_ = g2.Dijkstra(v0)
# for vertex in vertex_set:
#     print(f"Shortest distance from Source({v0}) and {vertex}: {dict_[vertex]}")


# v1 = Vertex(1)
# v2 = Vertex(2)
# v3 = Vertex(3)
# v4 = Vertex(4)
# v5 = Vertex(5)
# v6 = Vertex(6)
# v7 = Vertex(7)

# vertex_set = {v1, v2, v3, v4, v5, v6, v7}
# edge_set = {
#     Edge(v1, v2, 2),
#     Edge(v2, v5, 10),
#     Edge(v2, v4, 3),
#     Edge(v4, v5,2),
#     Edge(v4, v7, 4),
#     Edge(v5, v7, 6),
#     Edge(v4, v6, 8),
#     Edge(v7, v6, 1),
#     Edge(v3, v6, 5),
#     Edge(v4, v3, 2),
#     Edge(v1, v4, 1),
#     Edge(v3, v1, 4) 
# }
# g3 = DirectedGraph(vertex_set, edge_set)
# dijkstra_dict=g3.Dijkstra(v1) 
# print("------")
# for vertex in vertex_set:
#     print(f"Shortest distance from Source({v1}) and {vertex}: {dijkstra_dict[vertex]}")


# v_set2 = {v0, v1, v2, v3, v4}
# e_set2 = {
#     Edge(v0, v1, 2),
#     Edge(v0, v3, 6),
#     Edge(v1, v3, 8),
#     Edge(v1, v2, 3),
#     Edge(v1, v4, 5),
#     Edge(v2, v4, 7),
#     Edge(v3, v4, 9),
# }
# g2 = UndirectedGraph(v_set2, e_set2)

# g2.print_adjacency_list()

# mst2 = g2.prim_MST(v0)
# print("------")
# mst2.print_adjacency_list()

a = Vertex("a")
b = Vertex("b")
c = Vertex("c")
d = Vertex("d")
e = Vertex("e")
f = Vertex("f")
g = Vertex("g")
h = Vertex("h")
i = Vertex("i")
vertex_set = {a, b, c, d, e, f, g, h, i}
edge_set = {
    Edge(a, b, 4),
    Edge(b, c, 8),
    Edge(c, d, 7),
    Edge(d, e, 9),
    Edge(e, f, 10),
    Edge(f, g, 2),
    Edge(g, h, 1),
    Edge(h, a, 8),
    Edge(b, h, 11),
    Edge(c, i, 2),
    Edge(i, h, 7),
    Edge(i, g, 6),
    Edge(c, f, 4),
    Edge(d, f, 14),
}
g = UndirectedGraph(vertex_set, edge_set)
mst = g.prim_MST(a)
print("------")
mst.print_adjacency_list()
# ------------------------------------------------------- #
s = Vertex("s")
t = Vertex("t")
y = Vertex("y")
x = Vertex("x")
z = Vertex("z")

vertex_set2 = {s, t, y, x, z}
edge_set2 = {
    Edge(s, t, 10),
    Edge(t, x, 1),
    Edge(s, y, 5),
    Edge(z, s, 7),
    Edge(y, z, 2),
    Edge(y, t, 3),
    Edge(y, x, 9),
    Edge(x, z, 4),
    Edge(z, x, 6),
    Edge(t, y, 2),
}
g2 = DirectedGraph(vertex_set2, edge_set2)
dijkstra_dict = g2.Dijkstra(s)
print("------")
for vertex in vertex_set2:
    print(f"Shortest distance from Source({s}) and {vertex}: {dijkstra_dict[vertex]}")
