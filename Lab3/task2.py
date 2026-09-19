# 2 Depth First Search
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
def dfs(graph, node, visited):
  if node not in visited:
    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
      dfs(graph, neighbour, visited)
visited=set()
print("DFS Order:", end=" ")



dfs(graph, 'A', visited)