import pytest
from code_challenges.graph.graph import Graph

@pytest.mark.graph
def test_graph_creation():
  g = Graph()
  assert g.size == 0

@pytest.mark.graph
def test_add_node():
  g = Graph()
  g.add_node('a')
  g.add_node('b')
  result = g.get_node()
  assert result == ['a', 'b']

@pytest.mark.graph
def test_add_edge():
  g = Graph()
  g.add_node('a')
  g.add_node('b')
  g.add_node('kitten')
  g.add_edge('a', 'kitten')
  result = g.adjacency_list['a'][0].vertex
  assert result == 'kitten'

@pytest.mark.graph
def test_node_collection():
  g = Graph()
  g.add_node('a')
  g.add_node('b')
  g.add_node('c')
  g.add_node('kitten')
  assert g.get_node() == ['a', 'b', 'c', 'kitten']

@pytest.mark.graph
def test_node_collection():
  g = Graph()
  g.add_node('a')
  g.add_node('b')
  g.add_node('c')
  g.add_node('kitten')
  g.add_edge('c', 'kitten')
  g.add_edge('a', 'b')
  g.add_edge('a', 'c')
  g.add_edge('a', 'kitten', 4)

  result = g.get_neighbor('a')
  assert result == [('b', 1), ('c', 1), ('kitten', 4)]

@pytest.mark.graph
def test_graph_size():
  g = Graph()
  g.add_node('a')
  g.add_node('b')
  g.add_node('c')
  g.add_node('d')
  g.add_node('e')
  assert g.size == 5

@pytest.mark.graph
def test_graph_size_fail():
  g = Graph()
  g.add_node('a')
  g.add_node('b')
  assert g.size != 1

@pytest.mark.graph
def test_one_node():
  g = Graph()
  g.add_node('a')
  g.add_edge('a', 'a')
  result = g.get_node()
  assert result == ['a']

@pytest.mark.graph
def test_graph_empty():
  g = Graph()
  assert g.get_node() == None