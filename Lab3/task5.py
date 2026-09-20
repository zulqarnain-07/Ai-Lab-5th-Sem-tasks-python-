# 5
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'G'],
    'E': ['C'],
    'G': ['D']
}

heuristic = {
    'A': 7,
    'B': 4,
    'C': 6,
    'D': 2,
    'E': 5,
    'G': 0
}

current = 'A'

print("Starting at:", current, "Heuristic:", heuristic[current])

while heuristic[current] != 0:

    neighbors = graph[current]

    best_neighbor = min(neighbors, key=lambda node: heuristic[node])

    if heuristic[best_neighbor] < heuristic[current]:
        current = best_neighbor
        print("Move to:", current, "Heuristic:", heuristic[current])
    else:
        print("No better neighbor found.")
        break

print("Stopped at:", current, "Heuristic:", heuristic[current])
