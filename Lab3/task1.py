# Task 1: Breadth-First Search (BFS)
from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
def bfs(graph,start):
  visited = set()
  queue = deque([start])
  order = []
  while queue:
    node = queue.popleft()
    if node not in visited:
      visited.add(node)
      order.append(node)

      for neighbour in graph[node]:
        if neighbour not in visited:
          queue.append(neighbour)
  return order

result = bfs(graph, 'A')
print("BFS Traversal:", result)

