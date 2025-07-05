from collections import deque  # Import deque for efficient queue operations

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()  
        if node not in visited:
            print(node, end=" ") 
            visited.add(node)  
            
            
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)


# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F', 'G'],
#     'D': ['B'],
#     'E': ['B'],
#     'F': ['C'],
#     'G': ['C']
# }

graph = {}
num_nodes = int(input("Enter the number of nodes: "))

for _ in range(num_nodes):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (comma-separated): ").split(',')
    graph[node] = [neighbor.strip() for neighbor in neighbors]

# Taking user input for the starting node
start_node = input("Enter the starting node: ")

print("\nBFS Traversal:")
bfs(graph, start_node)

# bfs(graph, 'A')  # Start BFS traversal from node 'A'

# from collections import deque  # Import deque for efficient queue operations

# def bfs(graph, start):
#     visited = set()  # Keep track of visited nodes
#     queue = deque([start])  # Initialize queue with the starting node
    
#     while queue:
#         node = queue.popleft()  # Remove and process the first node in the queue
#         if node not in visited:
#             print(node, end=" ")  # Process the node (e.g., print it)
#             visited.add(node)  # Mark node as visited
            
#             # Add unvisited neighbors to the queue for future processing
#             queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# # Example usage: Define a graph as an adjacency list
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F', 'G'],
#     'D': ['B'],
#     'E': ['B'],
#     'F': ['C'],
#     'G': ['C']
# }

# # graph = {}
# # num_nodes = int(input("Enter the number of nodes: "))

# # for _ in range(num_nodes):
# #     node = input("Enter node: ")
# #     neighbors = input(f"Enter neighbors of {node} (comma-separated): ").split(',')
# #     graph[node] = [neighbor.strip() for neighbor in neighbors]

# # # Taking user input for the starting node
# # start_node = input("Enter the starting node: ")

# # print("\nBFS Traversal:")
# # bfs(graph, start_node)

# bfs(graph, 'A')  # Start BFS traversal from node 'A'
