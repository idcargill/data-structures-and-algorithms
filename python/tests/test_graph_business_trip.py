import pytest
from code_challenges.graph.graph import Graph
from code_challenges.graph_business_trip.graph_business_trip import business_trip

@pytest.fixture
def graph():
  graph = Graph()
  graph.add_node('A')
  graph.add_node('B')
  graph.add_node('C')
  graph.add_node('D')

  graph.add_edge('A', 'B', 50)
  graph.add_edge('B', 'C', 50)
  graph.add_edge('C', 'D', 50)
  return graph

@pytest.fixture
def arr():
  return ['A', 'B', 'C', 'D']

@pytest.mark.business
def test_business_trip(graph, arr):
  result = business_trip(graph, arr)
  assert result == 150


@pytest.mark.business
def test_business_trip_incorrect(graph, arr):
  result = business_trip(graph, arr)
  assert result != 100

@pytest.mark.business
def test_business_trip_should_false(graph):
  arr = ['A', 'D']
  result = business_trip(graph, arr)
  assert result == False