def bellman_ford(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                print("Graph contains a negative cycle")
                return None

    return distances

graph = {
    'A': {'B': 6, 'C': 4, 'D': 5},
    'B': {'E': -1},
    'C': {'B': -2, 'E': 3},
    'D': {'C': -2, 'F': -1},
    'E': {'F': 3},
    'F': {}
}

start_node = 'A'
shortest_distances = bellman_ford(graph, start_node)
if shortest_distances:
    print("Shortest distances from node", start_node + ":")
    for node, distance in shortest_distances.items():
        print("To", node + ":", distance)
