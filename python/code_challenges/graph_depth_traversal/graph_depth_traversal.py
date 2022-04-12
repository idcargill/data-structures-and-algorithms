from code_challenges.stack_and_queue.Stack import Stack
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



  def depth_traversal(self, vertex):
    stack = Stack()
    visited = []

    node = [item  for item in self.adjacency_list.keys()][0]


    if len(self.get_neighbor(vertex)) == 0:
      print('has no children')
      visited.append(node)
      return visited
    
    stack.push(vertex)

    while stack.is_empty() == False:
      if stack.peek() is not None:
        node = stack.pop()
        if node not in visited:
          visited.append(node)
          children = self.get_neighbor(node)
          for c in children:
            if c[0] not in visited:
              visited.append(c[0])
              stack.push(c[0]) 
    return visited


    
graph = Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')
graph.add_node('G')
graph.add_node('H')

graph.add_edge('A', 'B')
graph.add_edge('A', 'D')
graph.add_edge('B', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'G')
graph.add_edge('D', 'E')
graph.add_edge('D', 'H')
graph.add_edge('D', 'F')
graph.add_edge('H', 'F')


print(graph.depth_traversal('A'))
