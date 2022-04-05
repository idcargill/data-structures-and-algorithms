from code_challenges.stack_and_queue.Queue import Queue

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
    edge1 = self.Edge(vertex1, weight)
    edge2 = self.Edge(vertex2, weight)

    value1 = self.adjacency_list[vertex1]
    value2 = self.adjacency_list[vertex2]

    value1.append(edge2)
    value2.append(edge1)

    self.adjacency_list[vertex1] = value1
    self.adjacency_list[vertex2] = value2


  def get_node(self):
    if self.size == 0: 
      return None
    return list(self.adjacency_list.keys())
    
  def get_neighbor(self, vertex):
    neighbors = [(v.vertex, v.weight) for v in self.adjacency_list[vertex]]
    return neighbors
    
  def size(self):
    return self.size

  def breadth_traversal(self, vertex):
    Q = Queue()
    visited = []
    values = []

    if self.size == 0:
      return None
    
    Q.enqueue(vertex)
    
    while Q.is_empty() == False:
      # Dequeue
      vertex = Q.dequeue()
  
      if vertex not in visited:
        values.append(vertex)
        visited.append(vertex)
      
      if len(self.adjacency_list[vertex]) == 0:
        return None
        
      vert_children = [v for v in self.adjacency_list[vertex]]
      for child in vert_children:
        if child.vertex not in visited:
          Q.enqueue(child.vertex)

    return visited
