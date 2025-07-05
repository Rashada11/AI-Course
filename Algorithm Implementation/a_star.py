import heapq  # Priority queue for selecting best nodes

def a_star_search(graph, cost, heuristic, start, goal):
    priority_queue = []  # Min-heap to prioritize nodes based on f(n)
    heapq.heappush(priority_queue, (0 + heuristic[start], 0, start))  # Push start node
    visited = set()
    parent_map = {}  # Track parent nodes for path reconstruction

    while priority_queue:
        f, g, node = heapq.heappop(priority_queue)  # Get node with lowest f(n)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            print("\nGoal Found!")
            return reconstruct_path(parent_map, start, goal)

        for neighbor in graph[node]:  # Explore neighbors
            new_g = g + cost[(node, neighbor)]  # Calculate g(n) for neighbor
            f = new_g + heuristic[neighbor]  # Calculate f(n) for neighbor
            if neighbor not in visited:
                heapq.heappush(priority_queue, (f, new_g, neighbor))
                parent_map[neighbor] = node  # Store parent for path reconstruction

def reconstruct_path(parent_map, start, goal):
    """ Reconstructs the shortest path from start to goal using parent_map. """
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent_map[node]
    path.append(start)
    return list(reversed(path))

# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Example cost values (g(n))
cost = {
    ('A', 'B'): 1, ('A', 'C'): 3, ('B', 'D'): 1, ('B', 'E'): 4, ('C', 'F'): 2, ('C', 'G'): 1,
}

# Example heuristic values (h(n)) (lower = closer to goal 'G')
heuristic = {
    'A': 7, 'B': 4, 'C': 3, 'D': 5, 'E': 2, 'F': 1, 'G': 0
}

print("\nA* Search Traversal:")
path = a_star_search(graph, cost, heuristic, 'A', 'G')
print(f"Shortest Path: {path}")
