from code_challenges.graph.graph import Graph

def business_trip(graph, array):
  trip_total = 0
  possible = True
  recorded =[]

  for i in range(len(array)-1):
    neighbors = [city[0] for city in graph.get_neighbor(array[i])]
    weight = [city[1] for city in graph.get_neighbor(array[i])]
    if array[i+1] in neighbors and array[i+1]:
      if array[i+1] not in recorded:
        recorded.append(array[i])
        trip_total += weight[0]
    else:
      possible = False

  if possible:
    return trip_total
  return False


# graph = Graph()
# graph.add_node('A')
# graph.add_node('B')
# graph.add_node('C')
# graph.add_node('D')

# graph.add_edge('A', 'B', 50)
# graph.add_edge('B', 'C', 50)
# graph.add_edge('C', 'D', 50)

# business_trip(graph, ['A', 'B', 'C', 'D'])