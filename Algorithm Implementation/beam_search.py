import heapq  # Priority queue for selecting top-k paths

def beam_search(graph, heuristic, start, goal, beam_width):
    priority_queue = []  # Min-heap to select best paths
    heapq.heappush(priority_queue, (heuristic[start], [start]))  # Start node
    visited = set()

    while priority_queue:
        candidates = []  # Temporary storage for expanded nodes

        for _ in range(min(len(priority_queue), beam_width)):  # Consider top-k nodes
            _, path = heapq.heappop(priority_queue)  # Get the best path
            node = path[-1]

            if node in visited:
                continue
            visited.add(node)

            if node == goal:
                print("\nGoal Found!")
                return path  # Return best path to goal

            for neighbor in graph[node]:  # Expand neighbors
                new_path = path + [neighbor]
                heapq.heappush(candidates, (heuristic[neighbor], new_path))

        priority_queue = sorted(candidates)[:beam_width]  # Keep only top-k paths

    return None  # No path found

# Example graph structure
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Example heuristic values (lower = better)
heuristic = {
    'A': 7, 'B': 4, 'C': 3, 'D': 5, 'E': 2, 'F': 1, 'G': 0
}

# Running Beam Search with width = 2
start_node = 'A'
goal_node = 'G'
beam_width = 2

print("\nBeam Search Traversal:")
best_path = beam_search(graph, heuristic, start_node, goal_node, beam_width)
print(f"Best Found Path: {best_path}")
