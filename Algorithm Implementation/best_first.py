import heapq  

def best_first_search(graph, heuristic, start, goal):
    priority_queue = []  
    heapq.heappush(priority_queue, (heuristic[start], start)) 
    visited = set()

    while priority_queue:
        _, node = heapq.heappop(priority_queue) 

        if node in visited:
            continue
        visited.add(node)

        print(node, end=" ")  

        if node == goal:
            print("\nGoal Found!")
            return

        for neighbor in graph[node]:  # Explore neighbors
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))

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

# Example heuristic values (lower = closer to goal 'G')
heuristic = {
    'A': 7, 'B': 4, 'C': 3, 'D': 5, 'E': 2, 'F': 1, 'G': 0
}

print("\nBest-First Search Traversal:")
best_first_search(graph, heuristic, 'A', 'G')
