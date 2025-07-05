def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()  

    if node not in visited:
        print(node, end=" ")  
        visited.add(node)  

        
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Taking user input for graph definition
graph = {}
num_nodes = int(input("Enter the number of nodes: "))

for _ in range(num_nodes):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (comma-separated): ").split(',')
    graph[node] = [neighbor.strip() for neighbor in neighbors]

# User inputs the starting node
start_node = input("Enter the starting node: ")

print("\nDFS Traversal:")
dfs(graph, start_node)
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': [],
#     'E': [],
#     'F': [],
#     'G': []
# }

# # Starting DFS traversal from node 'A'
# print("\nDFS Traversal:")
# dfs(graph, 'A')




# def dfs(graph, node, visited=None):
#     if visited is None:
#         visited = set()  # Initialize the visited set if it's not passed in

#     if node not in visited:
#         print(node, end=" ")  # Process the node (e.g., print it)
#         visited.add(node)  # Mark node as visited

#         # Recursively visit each unvisited neighbor
#         for neighbor in graph[node]:
#             dfs(graph, neighbor, visited)

# # Taking user input for graph definition
# # graph = {}
# # num_nodes = int(input("Enter the number of nodes: "))

# # for _ in range(num_nodes):
# #     node = input("Enter node: ")
# #     neighbors = input(f"Enter neighbors of {node} (comma-separated): ").split(',')
# #     graph[node] = [neighbor.strip() for neighbor in neighbors]

# # # User inputs the starting node
# # start_node = input("Enter the starting node: ")

# # print("\nDFS Traversal:")
# # dfs(graph, start_node)
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': [],
#     'E': [],
#     'F': [],
#     'G': []
# }

# # Starting DFS traversal from node 'A'
# print("\nDFS Traversal:")
# dfs(graph, 'A')