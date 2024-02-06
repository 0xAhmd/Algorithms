def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Keep track of visited nodes
    visited = set()
    
    while len(visited) < len(graph):
        # Find the node with the smallest distance that has not been visited
        min_node = None
        min_distance = float('inf')
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_node = node
                min_distance = distances[node]
        
        # Mark the min_node as visited
        visited.add(min_node)
        
        # Update distances to neighbors of the min_node
        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    
    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node + ":")
for node, distance in shortest_distances.items():
    print("Node:", node, "- Distance:", distance)
