import heapq 

def best_first_search(graph, heuristic, start, goal):
    """ Best-First Search using a heuristic function """
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

        for neighbor in graph[node]: 
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Example heuristic values (lower values indicate proximity to goal 'G')
heuristic = {
    'A': 7, 'B': 4, 'C': 3, 'D': 5, 'E': 2, 'F': 1, 'G': 0  # Goal 'G' has heuristic 0
}

# Running the heuristic-based search
start_node = 'A'
goal_node = 'G'

print("\nBest-First Search Traversal:")
best_first_search(graph, heuristic, start_node, goal_node)
