class Graph:

  def __init__(self):
    self.adjacency_list = {}
    self.size = 0

  class Vertex:
    def __init__(self, value):
        self.value = value

  class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight


  def add_node(self, value):
    # Arguments: value
    # Returns: The added node
    # Add a node to the graph or add to adj list
    vert = self.Vertex(value)
    try:
      if vert.value in self.adjacency_list:
        raise Exception(f'Vertex {vert.value} already exists')
      self.adjacency_list[vert.value] = []
      self.size += 1
      return vert.value
    except Exception as e:
      print(e)
      return 0


  def add_edge(self, vertex1, vertex2, weight=1):
    # Arguments: 2 nodes to be connected by the edge, weight (optional)
    # Returns: nothing
    # Adds a new edge between two nodes in the graph
    # If specified, assign a weight to the edge
    # Both nodes should already be in the Graph
    
    edge1 = self.Edge(vertex1, weight)
    edge2 = self.Edge(vertex2, weight)

    value1 = self.adjacency_list[vertex1]
    value2 = self.adjacency_list[vertex2]

    value1.append(edge2)
    value2.append(edge1)

    self.adjacency_list[vertex1] = value1
    self.adjacency_list[vertex2] = value2

  def get_node(self):
    pass
    # Arguments: none
    # Returns all nodes in graph as a collection (set, list, or similar)

  def get_neighbor(self, vertex):
    pass
    # Arguments: node
    # Returns a collection of edges connected to the given node
    # Include the weight of connection in returned collection

  def size(self):
    # Arguments: none
    # Returns the total number of nodes in the graph
    return self.size



g = Graph()
g.add_node('a')
g.add_node('b')
g.add_node('b')

g.add_edge('a', 'b')


print(g.adjacency_list['a'][0].vertex)
print(g.adjacency_list['b'][0].vertex)

