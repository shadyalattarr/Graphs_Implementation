from abc import ABC, abstractmethod
from typing import Set, Dict, List

from edge import Edge
from vertex import Vertex


class Graph(ABC):

    def __init__(self, vertices: Set[Vertex], edges: Set[Edge]):
        self.vertices: Set[Vertex] = vertices
        self.edges: Set[Edge] = edges
        self.adj_dict: Dict[Vertex, List[Vertex]] = self._load_adjacency_list()

    @abstractmethod
    def _load_adjacency_list(self) -> Dict[Vertex, List[Vertex]]:
        pass

    def get_neighbors(self, vertex: Vertex) -> List[Vertex]:
        if vertex in self.vertices:
            return self.adj_dict[vertex.data]
        else:
            print(f"ERROR VERTEX {vertex} NOT IN GRAPH")
            return []

    def print_adjacency_list(self):
        for vertex, adjacent_vertices in self.adj_dict.items():
            print(f"{vertex}: [", end='')
            for i in adjacent_vertices:
                print(f"{i.data},", end='')
            print("]")


class UndirectedGraph(Graph):

    def _load_adjacency_list(self):
        # adjacency list is adj_dictionary
        adj_dictionary = {}  # empty dictionary
        for vertex in self.vertices:
            adj_dictionary[vertex.data] = []
            for edge in self.edges:
                if vertex in edge.vertices_pair:
                    adj_dictionary[vertex.data].append(edge.vertices_pair[0] if edge.vertices_pair[0] != vertex
                                                       else edge.vertices_pair[1])  # list of the vertex's neighbors
        return adj_dictionary



class DirectedGraph(Graph):

    def _load_adjacency_list(self):
        # adjacency list is adj_dictionary
        adj_dictionary = {}  # empty dictionary
        for vertex in self.vertices:
            adj_dictionary[vertex.data] = []
            for edge in self.edges:
                if vertex in edge.vertices_pair and vertex == edge.vertices_pair[0]:  # from the vertex--only difference
                    adj_dictionary[vertex.data].append(edge.vertices_pair[1])  # list of the vertex's neighbors
        return adj_dictionary
