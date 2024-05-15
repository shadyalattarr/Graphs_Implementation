I want to implement a Graph data Structure
it should allow for both directed and undirected graphs
I think i will make the Graph class a parent with directed_graph and undirected_graph as its children
and make different methods abstract, and common implemented

Graph should have->
1. load adjacency list
2. get neighbors of a certain vertex
3. print adjacency list

note: Adjacency list is a Dictionary with vertex data as keys and its value is a list of vertices (which are the key vertex's neighbors)
