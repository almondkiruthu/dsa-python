# Given a connected graph represented by a list of edges, where
# edge[0] = src, edge[1] = destination and edge[2] = weight,
# find the shortest path from source to every other node in the graph.
# There are n nodes in the graph.
# Time complexiy is 0(E * logV), 0(E * logE) is also correct.

import heapq

def shortest_path(edges, n, src):
  adjency_list = {}
  
  for source, destination, weight in edges:
    if source not in adjency_list:
      adjency_list[source] = []
    adjency_list[source].append((destination, weight))

    
  frontier = {}
  minHeap = [(0, src)]
  while len(minHeap) > 0:
    weight_1, node_1 = heapq.heappop(minHeap)
    if node_1 in frontier:
      # skip that node it has already been processed
      continue
    
    frontier[node_1] = weight_1
    neighbours = adjency_list.get(node_1, [])
    
    for neighbour, neighbour_weight in neighbours: 
      if neighbour not in frontier:
        heapq.heappush(minHeap, (weight_1 + neighbour_weight, neighbour))

  
  return frontier

edges = [
    ('A', 'B', 2),
    ('A', 'C', 4),
    ('B', 'C', 1),
    ('B', 'D', 7),
    ('C', 'E', 3),
    ('D', 'E', 1)
]
n = 5
src = 'A'


print(shortest_path(edges, n, src))