import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        for neighbor, weight in graph[node].items():
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist

# Example "India cities" graph (fake distances but valid)
graph = {
    "Delhi": {"Mumbai": 1400, "Kolkata": 1500},
    "Mumbai": {"Delhi": 1400, "Chennai": 1300},
    "Kolkata": {"Delhi": 1500, "Chennai": 1600},
    "Chennai": {"Mumbai": 1300, "Kolkata": 1600}
}

start = "Delhi"
print(dijkstra(graph, start))