import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = {node: False for node in graph}
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if visited[current_node]:
            continue
        visited[current_node] = True
        for neighbor, weight in graph[current_node].items():
            if not visited[neighbor]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
    return distances

graph = {
    'A': {'B': 4, 'E': 8},
    'B': {'A': 4, 'C': 8, 'E': 11},
    'C': {'B': 8, 'D': 7, 'G': 4, 'I': 2},
    'D': {'C': 7, 'G': 14, 'H': 9},
    'E': {'A': 8, 'B': 11, 'F': 1, 'I': 7},
    'F': {'E': 1, 'G': 2, 'I': 6},
    'G': {'C': 4, 'D': 14, 'F': 2, 'H': 10},
    'H': {'D': 9, 'G': 10},
    'I': {'C': 2, 'E': 7, 'F': 6}
}
start_node = 'A'

print(graph['A'].items())

shortest_distances = dijkstra(graph, start_node)
# for node, distance in shortest_distances.items():
#     print(f"{node} : {distance}")

# print(shortest_distances.keys())
# print(shortest_distances.values())
# for node, distance in shortest_distances.items():
#     print("To", node + ":", distance)
