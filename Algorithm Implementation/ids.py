def dls(graph, node, depth_limit, visited=None, depth=0):
    """ Depth-Limited Search (DLS) function """
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")  # Process the node
        visited.add(node)

        if depth < depth_limit:  # Stop if depth limit is reached
            for neighbor in graph[node]:
                dls(graph, neighbor, depth_limit, visited, depth + 1)

def ids(graph, start, max_depth):
    """ Iterative Deepening Search (IDS) function """
    for depth in range(max_depth + 1): 
        visited = set()
        print(f"\nIDS at Depth {depth}:")
        dls(graph, start, depth, visited)

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


max_depth = 3 
print("\nIterative Deepening Search (IDS) Traversal:")
ids(graph, 'A', max_depth)
