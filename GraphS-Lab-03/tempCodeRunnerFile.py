v0 = Vertex(0)
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
    
