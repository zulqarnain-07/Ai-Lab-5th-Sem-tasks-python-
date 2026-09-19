# 3 Greedy Best First Search
heuristic = {
    'A': 8,
    'B': 4,
    'C': 6,
    'D': 2,
    'Restaurant': 0
}
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['Restaurant'],
    'D': ['Restaurant'],
    'Restaurant': []
}
current = 'A'

while current != 'Restaurant':
    print("Current:", current)
    neighbors = graph[current]
    current = min(neighbors, key=lambda x: heuristic[x])

print("Reached: Restaurant")
