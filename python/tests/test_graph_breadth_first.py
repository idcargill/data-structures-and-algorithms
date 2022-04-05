import pytest
from code_challenges.graph_breadth_first.graph_breadth_first import Graph


@pytest.mark.graphB
def test_graph_instantiated():
  graph = Graph()
  assert graph.size == 0

@pytest.mark.graphB
def test_graph_breadth_no_edges():
  graph = Graph()
  graph.add_node('cat')
  graph.add_node('fish')
  result = graph.breadth_traversal('cat')
  assert result == None


@pytest.mark.graphB
def test_graph_breadth_():
  graph = Graph()
  graph.add_node('A')
  graph.add_node('B')
  graph.add_node('C')
  graph.add_node('D')
  graph.add_edge('A','B')
  graph.add_edge('A','D')
  result = graph.breadth_traversal('A')
  assert result == ['A', 'B', 'D']

@pytest.mark.graphB
def test_graph_breadth_2():
  graph = Graph()
  graph.add_node('A')
  graph.add_node('B')
  graph.add_node('C')
  graph.add_node('D')
  graph.add_edge('A','B')
  graph.add_edge('A','D')
  graph.add_edge('B', 'D')
  graph.add_edge('D', 'A')
  result = graph.breadth_traversal('A')
  assert result == ['A', 'B', 'D' ]