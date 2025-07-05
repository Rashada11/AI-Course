def dls(graph, node, depth_limit, visited=None, depth=0):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")  # Process the node
        visited.add(node)

        if depth < depth_limit:  # Check if depth limit is reached
            for neighbor in graph[node]:
                dls(graph, neighbor, depth_limit, visited, depth + 1)

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

depth_limit = 2  # Set a depth limit
print("\nDLS Traversal (Depth Limit = 2):")
dls(graph, 'A', depth_limit)
