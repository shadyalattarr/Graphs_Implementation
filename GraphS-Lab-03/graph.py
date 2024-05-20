from abc import ABC, abstractmethod
from typing import Set, Dict, List
import sys

from minheap import MinHeap
from edge import Edge
from vertex import Vertex


class Graph(ABC):

    def __init__(self, vertices: Set[Vertex], edges: Set[Edge]):
        if len(vertices) != 0:
            self.vertices: Set[Vertex] = vertices
            self.edges: Set[Edge] = edges
            self.adj_dict: Dict[Vertex, List[Vertex]] = self._load_adjacency_list()
        else:
            print("ERROR: CAN NOT HAVE AN EMPTY SET OF VERTICES")
            print("PLEASE REMAKE THE GRAPH WITH NON EMPTY SET OF VERTICES")

    @abstractmethod
    def _load_adjacency_list(self) -> Dict[Vertex, List[Vertex]]:
        pass

    @abstractmethod
    def get_edge(self, vertex_a: Vertex, vertex_b: Vertex):
        pass

    @abstractmethod
    def get_edge_cost(self, vertex_a, vertex_b) -> int:
        pass

    def Dijkstra(self, src: Vertex):
        heap = MinHeap(self.get_vertex_dictionary_prim(src))
        while not heap.isEmpty():
            min_weight_vertex = heap.get_and_remove_minimum()
            # print(heap.dictionary)
            # print(heap.heap)
            for adj_v in self.get_neighbors(min_weight_vertex):
                newDistance = heap.dictionary[min_weight_vertex] + self.get_edge_cost(min_weight_vertex, adj_v)
                if newDistance < heap.dictionary.get(adj_v, float('infinity')):
                    heap.dictionary[adj_v] = newDistance
                    heap.build_min_heap()
        return heap.dictionary

    # wont use?
    def get_vertex_dictionary_prim(self, src: Vertex):
        vertex_dict = {}
        for vertex in self.vertices:
            if src == vertex:
                vertex_dict[vertex] = 0
            else:
                vertex_dict[vertex] = sys.maxsize  # big number

        return vertex_dict

    def get_edge_dictionary(self):
        edge_dict = {}
        for edge in self.edges:
            edge_dict[edge] = edge.weight
        return edge_dict

    def get_neighbors(self, vertex: Vertex) -> List[Vertex]:
        if vertex in self.vertices:
            return self.adj_dict[vertex]
        else:
            print(f"ERROR VERTEX {vertex} NOT IN GRAPH")
            return []

    def print_adjacency_list(self):
        total_cost = 0
        for vertex, adjacent_vertices in self.adj_dict.items():
            print(f"{vertex}: [", end='')
            for i in adjacent_vertices:
                print(f"{i.data},", end='')
            print("]")

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xRoot = self.find(parent, x)
        yRoot = self.find(parent, y)
        if rank[xRoot] < rank[yRoot]:
            parent[xRoot] = yRoot
        elif rank[xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot
        else:
            parent[yRoot] = xRoot
            rank[xRoot] += 1


class UndirectedGraph(Graph):

    def Kruskal_MST(self):
        edges_list = list(self.edges)
        sorted_edges = sorted(edges_list, key=lambda edge: edge.weight)
        result = []
        parent_dict: Dict[Vertex, Vertex] = {}
        rank: Dict[Vertex, int] = {}
        for node in self.vertices:
            parent_dict[node] = node
            rank[node] = 0
        i = 0
        while i < len(self.edges):
            u, v, weight = sorted_edges[i].returnEdge()
            i += 1
            x = self.find(parent_dict, u)
            y = self.find(parent_dict, v)
            if x != y:
                result.append(Edge(u, v, weight))
                self.union(parent_dict, rank, x, y)

        return UndirectedGraph(self.vertices, set(result))

    def prim_MST(self, source: Vertex) -> Graph:
        heap = MinHeap(self.get_vertex_dictionary_prim(source))  # heap contains all vertices but with different
        # "weights" to vertex from connected component
        parent_dict: Dict[Vertex, Vertex] = {}  # parent to remember who's the node connected to min_vertex that
        # gave it the minweight
        mst_set = set()
        edge_set = set()
        mst_set.add(source)

        while len(mst_set) != len(self.vertices):  # while mst_set doesn't contain all vertices O(V)THIS E???
            min_weight_vertex = heap.get_and_remove_minimum()  # least "weight" to reach a new node
            if min_weight_vertex not in mst_set:
                mst_set.add(min_weight_vertex)  # connect to component
                edge_set.add(self.get_edge(parent_dict[min_weight_vertex], min_weight_vertex))  # edge

            #  need to add the new adj_vertices to heap dict
            adj_vertices = self.get_neighbors(min_weight_vertex)
            for adj_v in adj_vertices:  # adjacent vertices to newly added vertex--EE/
                if adj_v not in mst_set:  # if not already there
                    cost = self.get_edge_cost(min_weight_vertex, adj_v)
                    if cost < heap.dictionary[adj_v]:
                        heap.dictionary[adj_v] = cost
                        parent_dict[adj_v] = min_weight_vertex
                        heap.build_min_heap()  # to rebuild heap
        return UndirectedGraph(mst_set, edge_set)

    def _load_adjacency_list(self):
        # adjacency list is adj_dictionary
        adj_dictionary = {}  # empty dictionary
        for vertex in self.vertices:
            adj_dictionary[vertex] = []
            for edge in self.edges:
                if vertex in edge.vertices_pair:
                    adj_dictionary[vertex].append(edge.vertices_pair[0] if edge.vertices_pair[0] != vertex
                                                  else edge.vertices_pair[1])  # list of the vertex's neighbors
        return adj_dictionary

    def get_total_cost(self):
        total_cost = 0
        for vertex, adjacent_vertices in self.adj_dict.items():
            for i in adjacent_vertices:
                total_cost += self.get_edge_cost(vertex, i)
        return total_cost // 2

    def get_edge(self, vertex_a: Vertex, vertex_b: Vertex):
        for edge in self.edges:
            vertices = edge.vertices_pair
            if (vertex_a, vertex_b) == vertices or (vertex_b, vertex_a) == vertices:
                return edge
        return False

    def get_edge_cost(self, vertex_a, vertex_b) -> int:
        edg = self.get_edge(vertex_a, vertex_b)
        if edg:  # it exists
            return edg.weight


class DirectedGraph(Graph):

    def _load_adjacency_list(self):
        # adjacency list is adj_dictionary
        adj_dictionary = {}  # empty dictionary
        for vertex in self.vertices:
            adj_dictionary[vertex] = []
            for edge in self.edges:
                if vertex in edge.vertices_pair and vertex == edge.vertices_pair[0]:  # from the vertex--only difference
                    adj_dictionary[vertex].append(edge.vertices_pair[1])  # list of the vertex's neighbors

        return adj_dictionary

    def get_edge(self, src: Vertex, dest: Vertex):
        for edge in self.edges:
            vertices = edge.vertices_pair
            if (src, dest) == vertices:
                return edge
        return False

    def get_edge_cost(self, vertex_a, vertex_b) -> int:
        edg = self.get_edge(vertex_a, vertex_b)
        if edg:  # it exists
            return edg.weight
