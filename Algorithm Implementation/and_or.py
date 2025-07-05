def and_or_search(node, graph, path):
    # If node is goal (no successors), return solved
    if node not in graph or len(graph[node]) == 0:
        return "SOLVED"

    if node in path:
        return "FAIL"  # avoid loops

    node_type = None
    # If children have 'AND' or 'OR' type, get node_type
    # Here, we assume node_type is the type of first child's second value
    # In practice, node's type can be defined separately
    if len(graph[node]) > 0:
        node_type = graph[node][0][1]

    if node_type == 'OR':
        # OR node: try each child until one succeeds
        for (child, _) in graph[node]:
            result = and_or_search(child, graph, path + [node])
            if result != "FAIL":
                return {child: result}
        return "FAIL"

    elif node_type == 'AND':
        # AND node: all children must succeed
        results = {}
        for (child, _) in graph[node]:
            result = and_or_search(child, graph, path + [node])
            if result == "FAIL":
                return "FAIL"
            results[child] = result
        return results

    else:
        # If node has no type, treat as OR node with no children = goal
        return "SOLVED"


# Define the AND-OR graph
graph = {
    'A': [('B', 'OR'), ('C', 'AND')],
    'B': [('D', 'OR')],
    'C': [('E', 'AND'), ('F', 'AND')],
    'D': [],
    'E': [],
    'F': []
}

# Run the AND-OR search starting from node 'A'
solution = and_or_search('A', graph, [])

import pprint
pprint.pprint(solution)
