from collections import deque

def bidirectional_search(graph, start, goal):
    # Initialize two queues for forward and backward search
    forward_queue = deque([start])
    backward_queue = deque([goal])
    
    # Initialize visited sets for both directions
    visited_forward = {start}
    visited_backward = {goal}

    while forward_queue and backward_queue:
       
        if forward_queue:
            node = forward_queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited_forward:
                    forward_queue.append(neighbor)
                    visited_forward.add(neighbor)
                if neighbor in visited_backward:  # Meeting point found!
                    return f"Path found at {neighbor}"




        # Expand from the goal node (backward search)
        if backward_queue:
            node = backward_queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited_backward:
                    backward_queue.append(neighbor)
                    visited_backward.add(neighbor)
                if neighbor in visited_forward:  # Meeting point found!
                    return f"Path found at {neighbor}"

    return "No path found"

# Example graph (predefined without user input)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E', 'G'],
    'G': ['F']
}

start_node = 'A'
goal_node = 'G'

print("\nBidirectional Search Result:")
print(bidirectional_search(graph, start_node, goal_node))
